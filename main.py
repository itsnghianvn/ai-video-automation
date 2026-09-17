import subprocess


def run_step(name, command):
    print(f"\n{'=' * 50}")
    print(name)
    print(f"{'=' * 50}\n")

    subprocess.run(command, check=True)


def main():
    topic = input("Enter video topic: ").strip()

    if not topic:
        print("Topic cannot be empty.")
        return

    # Generate script
    run_step(
        "STEP 1: GENERATING SCRIPT",
        ["python", "gen_script.py", topic],
    )

    # Generate voice
    run_step(
        "STEP 2: GENERATING VOICE",
        ["python", "gen_voice.py"],
    )

    # Generate video
    run_step(
        "STEP 3: GENERATING VIDEO",
        ["python", "gen_video.py"],
    )

    print("\n" + "=" * 50)
    print("PIPELINE COMPLETED")
    print("=" * 50)
    print("Output: output.mp4")


if __name__ == "__main__":
    main()