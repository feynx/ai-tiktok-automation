import os
import uuid
import requests

OUTPUT_DIR = "output/visuals"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def fetch_ai_image(keyword):

    # Example using Pollinations (free AI image)
    url = f"https://image.pollinations.ai/prompt/{keyword}"

    filename = f"{uuid.uuid4()}.jpg"
    filepath = os.path.join(OUTPUT_DIR, filename)

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("AI image generation failed")

    with open(filepath, "wb") as f:
        f.write(response.content)

    return filepath
