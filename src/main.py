import os
from dotenv import load_dotenv
load_dotenv()

from generate_script import generate_script
from script_cleaner import clean_script
from hook_generator import generate_hook
from scene_classifier import classify_scenes
from voice_generator import generate_voice
from visual_fetcher import fetch_visual
from video_generator import build_scene_clip, merge_clips


OUTPUT_AUDIO = "output/audio"
OUTPUT_FINAL = "output/final"

os.makedirs(OUTPUT_AUDIO, exist_ok=True)
os.makedirs(OUTPUT_FINAL, exist_ok=True)


def main():

    topic = "Beautiful Myanmar Country"

    print("Generating Script...")
    script = generate_script(topic)

    print("Cleaning Script...")
    cleaned_script = clean_script(script)

    print("Classifying scenes...")
    scenes = classify_scenes(cleaned_script)

    clips = []

    for i, scene in enumerate(scenes):

        print(f"Processing Scene {i}")

        narration = scene["narration"]
        keywords = scene["keywords"]

        audio_path = f"{OUTPUT_AUDIO}/scene_{i}.mp3"

        generate_voice(narration, audio_path)

        visual_path = fetch_visual(keywords)

        clip = build_scene_clip(audio_path, visual_path)

        clips.append(clip)

    print("Merging Final Video...")

    final_video = f"{OUTPUT_FINAL}/final_video.mp4"

    merge_clips(clips, final_video)

    print("DONE:", final_video)


if __name__ == "__main__":
    main()
