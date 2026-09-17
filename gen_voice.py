import asyncio
import edge_tts


TEXT = """
Hello everyone.

Today, we are going to learn three interesting facts about space.

The universe is incredibly large, and there are billions of galaxies.
"""


async def generate_voice():
    voice = "en-US-AriaNeural"

    communicate = edge_tts.Communicate(
        TEXT,
        voice
    )

    await communicate.save("voice.mp3")


if __name__ == "__main__":
    asyncio.run(generate_voice())