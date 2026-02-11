from stock_fetcher import fetch_stock_video
from ai_image_fetcher import fetch_ai_image


def fetch_visual(keywords):

    keyword = keywords[0]

    try:
        return fetch_stock_video(keyword)
    except:
        return fetch_ai_image(keyword)
