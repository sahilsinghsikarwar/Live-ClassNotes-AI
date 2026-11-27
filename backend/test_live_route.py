
import asyncio
import json
import websockets

async def main():
    url = "ws://127.0.0.1:8000/live/transcribe"

    try:
        async with websockets.connect(url) as ws:
            response = await asyncio.wait_for(ws.recv(), timeout=30)
            print("Server response:", json.loads(response))

    except Exception as e:
        print("Connection failed:", e)

asyncio.run(main())
