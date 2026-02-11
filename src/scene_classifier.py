import re

# -----------------------------
# Remove unwanted symbols
# -----------------------------
def clean_sentence(text):

    # Remove hashtags / notes / stage directions
    text = re.sub(r'#.*', '', text)

    # Remove brackets notes
    text = re.sub(r'\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


# -----------------------------
# Split script into natural sentences
# -----------------------------
def split_into_sentences(script):

    script = clean_sentence(script)

    sentences = re.split(r'(?<=[.!?])\s+', script)

    return [s.strip() for s in sentences if len(s.strip()) > 3]


# -----------------------------
# Remove filler / stop words
# -----------------------------
STOP_WORDS = {
    "the","a","an","is","are","was","were","to","and","of",
    "in","on","at","for","with","by","from","that","this",
    "it","as","be","can","will","now","today"
}


# -----------------------------
# Smart keyword extraction
# -----------------------------
def extract_keywords(sentence, max_keywords=3):

    # Remove punctuation
    sentence = re.sub(r'[^\w\s]', '', sentence)

    words = sentence.lower().split()

    # Remove stop words
    filtered = [w for w in words if w not in STOP_WORDS and len(w) > 2]

    # Prioritize nouns / tech words style
    keywords = []

    for word in filtered:
        if word not in keywords:
            keywords.append(word)

        if len(keywords) >= max_keywords:
            break

    # fallback
    if not keywords:
        keywords = filtered[:max_keywords]

    return keywords


# -----------------------------
# Break long sentences into smaller visual beats
# -----------------------------
def split_long_sentence(sentence, max_words=12):

    words = sentence.split()

    if len(words) <= max_words:
        return [sentence]

    chunks = []
    for i in range(0, len(words), max_words):
        chunk = " ".join(words[i:i + max_words])
        chunks.append(chunk)

    return chunks


# -----------------------------
# Main classifier
# -----------------------------
def classify_scenes(script):

    base_sentences = split_into_sentences(script)

    scenes = []

    for sentence in base_sentences:

        # Break long narration for TikTok pacing
        chunks = split_long_sentence(sentence)

        for chunk in chunks:

            keywords = extract_keywords(chunk)

            scene = {
                "narration": chunk,
                "keywords": keywords
            }

            scenes.append(scene)

    return scenes
