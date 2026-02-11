import os
import requests
import uuid
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

OUTPUT_DIR = "output/visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fetch_stock_video(keyword):

    url = "https://api.pexels.com/videos/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": keyword,
        "per_page": 5
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception("Pexels API error")

    data = response.json()

    videos = data.get("videos")

    if not videos:
        raise Exception("No stock videos found")

    video_files = videos[0]["video_files"]

    # TikTok friendly vertical filter
    vertical_videos = [
        v for v in video_files
        if v["height"] > v["width"]
    ]

    if vertical_videos:
        best_video = sorted(
            vertical_videos,
            key=lambda x: x["width"] * x["height"],
            reverse=True
        )[0]
    else:
        best_video = sorted(
            video_files,
            key=lambda x: x["width"] * x["height"],
            reverse=True
        )[0]

    video_url = best_video["link"]

    return download_video(video_url)


def download_video(video_url):

    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join(OUTPUT_DIR, filename)

    video_data = requests.get(video_url).content

    with open(filepath, "wb") as f:
        f.write(video_data)

    return filepath
