import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_script(topic):

    prompt = f"""
Write a viral TikTok narration script about {topic}.

Rules:
- Strong hook first 2 seconds
- Short punchy sentences
- 45-60 seconds long
- Modern tech vibe
- End with engagement call
- Return narration only
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )

    return completion.choices[0].message.content
