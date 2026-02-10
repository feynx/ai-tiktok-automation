def classify_scene(text):

    if "phone" in text or "tech" in text:
        return "stock"

    if "funny" in text or "joke" in text:
        return "gif"

    return "ai_image"
