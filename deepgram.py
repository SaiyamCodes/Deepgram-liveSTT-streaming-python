import asyncio
import json
import os
import sys

import pyaudio
import websockets
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("DEEPGRAM_API_KEY")

if not API_KEY:
    raise RuntimeError("❌ DEEPGRAM_API_KEY missing")

# 1. Chunk Size: 2048 or 4096 is often better for network efficiency than 1024
RATE = 16000
CHUNK = 2048 

# 2. Optimized URL Parameters
DEEPGRAM_URL = (
    "wss://api.deepgram.com/v1/listen"
    "?encoding=linear16"
    "&sample_rate=16000"
    "&channels=1"
    "&model=nova-2"           # Fastest model
    "&interim_results=true"   # crucial for speed
    "&smart_format=true"      # fast enough, makes text readable
    "&endpointing=300"        # Return final result faster (after 300ms silence)
)

HEADERS = {
    "Authorization": f"Token {API_KEY}"
}

async def send_audio(ws):
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=RATE,
        input=True,
        frames_per_buffer=CHUNK,
    )

    print("🎙️ Listening...")
    
    # Get current event loop
    loop = asyncio.get_running_loop()

    try:
        while True:
            # 3. NON-BLOCKING READ
            # stream.read() is blocking. We run it in a separate thread so
            # the receive_text function doesn't freeze while waiting for mic input.
            data = await loop.run_in_executor(
                None, 
                lambda: stream.read(CHUNK, exception_on_overflow=False)
            )
            await ws.send(data)
    except websockets.exceptions.ConnectionClosed:
        print("\n⚠️ Connection closed")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

async def receive_text(ws):
    try:
        async for msg in ws:
            result = json.loads(msg)
            if "channel" in result:
                alternatives = result["channel"]["alternatives"]
                if alternatives:
                    transcript = alternatives[0]["transcript"]
                    is_final = result.get("is_final")

                    # 4. Optimized Printing
                    # Use \r to overwrite the line for interim results (looks faster)
                    if transcript:
                        if is_final:
                            # Final sentence, print on new line
                            sys.stdout.write(f"\r✅ {transcript}\n")
                        else:
                            # Interim result, overwrite current line
                            sys.stdout.write(f"\r⏳ {transcript}...")
                        sys.stdout.flush()
    except Exception as e:
        print(f"\nError receiving: {e}")

async def main():
    async with websockets.connect(
        DEEPGRAM_URL,
        extra_headers=HEADERS,
        ping_interval=5,
        ping_timeout=20,
    ) as ws:
        await asyncio.gather(
            send_audio(ws),
            receive_text(ws),
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
