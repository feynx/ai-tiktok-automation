import os
import random
from moviepy.editor import (
    AudioFileClip,
    ImageClip,
    ColorClip,
    concatenate_videoclips
)



def generate_video(voice_file):

    audio = AudioFileClip(voice_file)
    duration = audio.duration

    image_folder = "assets/images"

    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    images = [
        os.path.join(image_folder, img)
        for img in os.listdir(image_folder)
        if img.lower().endswith((".jpg", ".png", ".jpeg"))
    ]

    if len(images) == 0:
        video = ColorClip(size=(1080,1920), color=(0,0,0), duration=duration)
        video = video.set_audio(audio)

        output = "final_video.mp4"
        video.write_videofile(output, fps=24)
        return output

    random.shuffle(images)

    scene_duration = 3
    clips = []

    current_time = 0
    index = 0

    while current_time < duration:

        img_path = images[index % len(images)]

        clip = (
            ImageClip(img_path)
            .set_duration(scene_duration)
            .resize(height=1920)
            .set_position("center")
        )

        clips.append(clip)

        current_time += scene_duration
        index += 1

    video = concatenate_videoclips(clips)
    video = video.subclip(0, duration)
    video = video.set_audio(audio)

    output = "final_video.mp4"
    video.write_videofile(output, fps=24)

    return output
