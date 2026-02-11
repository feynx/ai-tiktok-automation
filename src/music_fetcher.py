import os
import random

MUSIC_DIR = "assets/music"

def get_background_music():

    files = [
        f for f in os.listdir(MUSIC_DIR)
        if f.endswith(".mp3")
    ]

    chosen = random.choice(files)

    return os.path.join(MUSIC_DIR, chosen)
