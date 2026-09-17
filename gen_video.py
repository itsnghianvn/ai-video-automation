import subprocess


IMAGES = [
    "images/galaxy.jpg",
    "images/earth.jpg",
    "images/astronaut.jpg",
]

VOICE = "voice.mp3"
OUTPUT = "output.mp4"

TRANSITION_DURATION = 1


def get_audio_duration():
    command = [
        "ffprobe",
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=noprint_wrappers=1:nokey=1",
        VOICE,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=True,
    )

    return float(result.stdout.strip())


def create_scene(image, output, duration):
    command = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-i",
        image,
        "-t",
        str(duration),
        "-vf",
        "scale=1280:720,setsar=1",
        "-c:v",
        "libx264",
        "-tune",
        "stillimage",
        "-pix_fmt",
        "yuv420p",
        output,
    ]

    subprocess.run(command, check=True)


def merge_scenes(scene_duration):
    offset_1 = scene_duration - TRANSITION_DURATION
    offset_2 = (scene_duration * 2) - (TRANSITION_DURATION * 2)

    filter_complex = (
        f"[0:v][1:v]xfade="
        f"transition=fade:"
        f"duration={TRANSITION_DURATION}:"
        f"offset={offset_1}[v01];"
        f"[v01][2:v]xfade="
        f"transition=fade:"
        f"duration={TRANSITION_DURATION}:"
        f"offset={offset_2}[v]"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i",
        "scene1.mp4",
        "-i",
        "scene2.mp4",
        "-i",
        "scene3.mp4",
        "-filter_complex",
        filter_complex,
        "-map",
        "[v]",
        "-c:v",
        "libx264",
        "-pix_fmt",
        "yuv420p",
        "merged.mp4",
    ]

    subprocess.run(command, check=True)


def add_voice():
    command = [
        "ffmpeg",
        "-y",
        "-i",
        "merged.mp4",
        "-i",
        VOICE,
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-shortest",
        OUTPUT,
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    audio_duration = get_audio_duration()

    scene_duration = audio_duration / len(IMAGES)

    print(f"Voice duration: {audio_duration:.2f}s")
    print(f"Number of scenes: {len(IMAGES)}")
    print(f"Scene duration: {scene_duration:.2f}s")

    for index, image in enumerate(IMAGES, start=1):
        output = f"scene{index}.mp4"

        print(f"Creating scene {index}...")
        create_scene(image, output, scene_duration)

    print("Merging scenes...")
    merge_scenes(scene_duration)

    print("Adding voice...")
    add_voice()

    print("Video created successfully:", OUTPUT)