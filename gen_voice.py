import asyncio

import edge_tts


INPUT_FILE = "script.txt"
OUTPUT_FILE = "voice.mp3"

VOICE = "en-US-AriaNeural"


async def generate_voice():
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        text = file.read()

    communicate = edge_tts.Communicate(text, VOICE)

    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    asyncio.run(generate_voice())

    print("Voice generated successfully:", OUTPUT_FILE)