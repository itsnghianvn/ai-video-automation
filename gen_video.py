import subprocess

IMAGES = [
    "images/galaxy.jpg",
    "images/earth.jpg",
    "images/astronaut.jpg",
]

VOICE = "voice.mp3"
OUTPUT = "output.mp4"

SCENE_DURATION = 4


def create_scene(image, output):
    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image,
        "-t", str(SCENE_DURATION),
        "-vf", "scale=1280:720,setsar=1",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-pix_fmt", "yuv420p",
        output,
    ]

    subprocess.run(command, check=True)


def merge_scenes():
    command = [
        "ffmpeg",
        "-y",
        "-i", "scene1.mp4",
        "-i", "scene2.mp4",
        "-i", "scene3.mp4",
        "-filter_complex",
        "[0:v][1:v][2:v]concat=n=3:v=1:a=0[v]",
        "-map", "[v]",
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "merged.mp4",
    ]

    subprocess.run(command, check=True)


def add_voice():
    command = [
        "ffmpeg",
        "-y",
        "-i", "merged.mp4",
        "-i", VOICE,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        OUTPUT,
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    create_scene(IMAGES[0], "scene1.mp4")
    create_scene(IMAGES[1], "scene2.mp4")
    create_scene(IMAGES[2], "scene3.mp4")

    merge_scenes()
    add_voice()

    print("Video created successfully:", OUTPUT)