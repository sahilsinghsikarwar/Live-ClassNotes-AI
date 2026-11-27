
import os
import json
import base64
import asyncio

import websockets
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "models/gemini-3.5-transcribe-live"

router = APIRouter(tags=["Live Transcription"])


@router.websocket("/live/transcribe")
async def live_transcription(websocket: WebSocket):
    await websocket.accept()

    if not API_KEY:
        await websocket.send_json({
            "type": "error",
            "message": "GEMINI_API_KEY not found"
        })
        await websocket.close()
        return

    url = (
        "wss://generativelanguage.googleapis.com/ws/"
        "google.ai.generativelanguage.v1beta."
        "GenerativeService.BidiGenerateContent"
        f"?key={API_KEY}"
    )

    try:
        async with websockets.connect(url) as gemini:

            setup = {
                "setup": {
                    "model": MODEL,
                    "generationConfig": {
                        "responseModalities": ["TEXT"]
                    },
                    "inputAudioTranscription": {}
                }
            }

            await gemini.send(json.dumps(setup))

            response = json.loads(await gemini.recv())

            if "setupComplete" not in response:
                raise Exception(f"Gemini setup failed: {response}")

            await websocket.send_json({"type": "ready"})

            async def send_audio():
                while True:
                    message = await websocket.receive_text()
                    data = json.loads(message)

                    if data.get("type") == "stop":
                        await gemini.send(json.dumps({
                            "realtimeInput": {
                                "audioStreamEnd": True
                            }
                        }))
                        return

                    if data.get("type") == "audio":
                        audio_message = {
                            "realtimeInput": {
                                "audio": {
                                    "data": data["audio"],
                                    "mimeType": "audio/pcm;rate=16000"
                                }
                            }
                        }

                        await gemini.send(json.dumps(audio_message))

            async def receive_transcript():
                while True:
                    raw_response = await gemini.recv()
                    result = json.loads(raw_response)

                    if "error" in result:
                        await websocket.send_json({
                            "type": "error",
                            "message": str(result["error"])
                        })
                        return

                    content = result.get("serverContent", {})

                    interim = content.get(
                        "interimInputTranscription", {}
                    ).get("text")

                    final = content.get(
                        "inputTranscription", {}
                    ).get("text")

                    if interim:
                        await websocket.send_json({
                            "type": "interim",
                            "text": interim
                        })

                    if final:
                        await websocket.send_json({
                            "type": "transcript",
                            "text": final
                        })

                    if content.get("turnComplete"):
                        return

            sender = asyncio.create_task(send_audio())
            receiver = asyncio.create_task(receive_transcript())

            try:
                done, pending = await asyncio.wait(
                    [sender, receiver],
                    return_when=asyncio.FIRST_COMPLETED
                )

                if sender in done:
                    await sender
                    if not receiver.done():
                        await receiver
                else:
                    await receiver

            finally:
                for task in (sender, receiver):
                    if not task.done():
                        task.cancel()

                await asyncio.gather(
                    sender, receiver, return_exceptions=True
                )

    except WebSocketDisconnect:
        print("Browser disconnected")

    except Exception as e:
        print("Live transcription error:", str(e))
        try:
            await websocket.send_json({
                "type": "error",
                "message": str(e)
            })
        except Exception:
            pass
