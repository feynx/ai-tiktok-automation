import asyncio
import edge_tts

VOICE = "en-US-JennyNeural"


async def generate_voice_async(text, filename):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(filename)


def generate_voice(text, filename):
    asyncio.run(generate_voice_async(text, filename))
    return filename
