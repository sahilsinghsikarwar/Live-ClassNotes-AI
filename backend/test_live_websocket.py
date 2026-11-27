
import os
import json
import asyncio
from pathlib import Path
from dotenv import load_dotenv
import websockets

load_dotenv(Path(__file__).resolve().parent / ".env")

API_KEY = os.getenv("GEMINI_API_KEY")

URL = (
    "wss://generativelanguage.googleapis.com/ws/"
    "google.ai.generativelanguage.v1beta.GenerativeService."
    "BidiGenerateContent?key=" + API_KEY
)

async def test_connection():
    async with websockets.connect(URL) as ws:
        print("WebSocket connected!")

        setup = {
            "setup": {
                "model": "models/gemini-3.5-transcribe-live",
                "generationConfig": {
                    "responseModalities": ["TEXT"]
                },
                "inputAudioTranscription": {
                    "languageCodes": []
                }
            }
        }

        await ws.send(json.dumps(setup))

        response = await asyncio.wait_for(
            ws.recv(),
            timeout=15
        )

        print("Gemini response:", response)

asyncio.run(test_connection())
