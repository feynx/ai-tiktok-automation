from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    ImageClip,
    ColorClip,
    CompositeVideoClip,
    concatenate_videoclips
)

from moviepy.audio.AudioClip import CompositeAudioClip

from music_fetcher import get_background_music

WIDTH = 1080
HEIGHT = 1920
FPS = 30


# ---------------------------------------
# Normalize visual into TikTok frame
# ---------------------------------------
def normalize_clip(clip, duration):

    # Resize visual safely
    clip = clip.resize(height=HEIGHT)

    # Black background (TikTok vertical safe)
    background = ColorClip(size=(WIDTH, HEIGHT), color=(0, 0, 0))
    background = background.set_duration(duration)

    # Center visual
    clip = clip.set_position("center")

    final = CompositeVideoClip([background, clip])

    final = final.set_duration(duration)
    final = final.set_fps(FPS)

    return final


# ---------------------------------------
# Background music mixer
# ---------------------------------------
def add_background_music(voice_audio):

    try:
        music_path = get_background_music()

        music = AudioFileClip(music_path)

        # Lower music volume
        music = music.volumex(0.15)

        # Match voice duration
        music = music.set_duration(voice_audio.duration)

        # Mix voice + music
        final_audio = CompositeAudioClip([music, voice_audio])

        return final_audio

    except Exception as e:
        print("Music load failed:", e)
        return voice_audio


# ---------------------------------------
# Build scene clip
# ---------------------------------------
def build_scene_clip(audio_path, visual_path):

    voice_audio = AudioFileClip(audio_path)

    # Detect visual type
    if visual_path.lower().endswith(".mp4"):
        visual = VideoFileClip(visual_path)

    elif visual_path.lower().endswith(".gif"):
        visual = VideoFileClip(visual_path)

    else:
        visual = ImageClip(visual_path)

    # Normalize visual size + duration
    visual = normalize_clip(visual, voice_audio.duration)

    # Add background music
    final_audio = add_background_music(voice_audio)

    visual = visual.set_audio(final_audio)

    return visual


# ---------------------------------------
# Merge all scene clips
# ---------------------------------------
def merge_clips(clips, output_path):

    final = concatenate_videoclips(clips, method="compose")

    final = final.set_fps(FPS)

    final.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        fps=FPS
    )

    return output_path
