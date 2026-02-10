from dotenv import load_dotenv
import os

load_dotenv()

from generate_script import generate_script
from voice_generator import generate_voice
from video_generator import generate_video


def main():
    topic = input("Enter TikTok topic: ")

    # Step 1 - Script Generate
    script = generate_script(topic)
    print("\nGenerated Script:\n")
    print(script)

    # Step 2 - Voice Generate
    voice_file = generate_voice(script)
    print("Voice generated:", voice_file)

    # Step 3 - Video Generate
    video_file = generate_video(voice_file)
    print("Video generated:", video_file)


if __name__ == "__main__":
    main()
