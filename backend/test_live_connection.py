
import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv(Path(__file__).resolve().parent / ".env")

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

async def test_connection():
    config = types.LiveConnectConfig(
        response_modalities=["TEXT"],
        input_audio_transcription=types.AudioTranscriptionConfig(
            language_codes=[]
        )
    )

    async with client.aio.live.connect(
        model="gemini-3.5-transcribe-live",
        config=config
    ) as session:
        print("Gemini Live API connected successfully!")

try:
    asyncio.run(test_connection())
except Exception as e:
    print("\nERROR TYPE:", type(e).__name__)
    print("ERROR DETAILS:", repr(e))
    response = getattr(e, "response", None)
    if response:
        print("SERVER RESPONSE:", getattr(response, "body", None))
