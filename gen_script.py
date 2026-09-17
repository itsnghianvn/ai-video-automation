import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def generate_script(topic):
    prompt = f"""
Write a short narration script for a video about:

{topic}

Requirements:
- 80-120 words
- Natural spoken English
- Interesting opening
- Easy to understand
- No markdown
- No title
- No bullet points
"""

    interaction = client.interactions.create(
        model="gemini-3.6-flash",
        input=prompt,
    )

    return interaction.output_text.strip()


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python gen_script.py <topic>")
        sys.exit(1)

    topic = " ".join(sys.argv[1:])

    script = generate_script(topic)

    print("\nGenerated script:\n")
    print(script)

    with open("script.txt", "w", encoding="utf-8") as file:
        file.write(script)

    print("\nScript saved to script.txt")