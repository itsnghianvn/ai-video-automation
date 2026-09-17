import subprocess


IMAGE = "images/galaxy.jpg"
VOICE = "voice.mp3"
OUTPUT = "output.mp4"


command = [
    "ffmpeg",
    "-loop", "1",
    "-i", IMAGE,
    "-i", VOICE,
    "-vf", "scale=622:320",
    "-c:v", "libx264",
    "-tune", "stillimage",
    "-c:a", "aac",
    "-pix_fmt", "yuv420p",
    "-shortest",
    OUTPUT,
]


subprocess.run(command, check=True)