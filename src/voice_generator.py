import asyncio
import edge_tts

VOICE = "en-US-JennyNeural"

async def generate_voice_async(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")

def generate_voice(text):
    asyncio.run(generate_voice_async(text))
    return "voice.mp3"
