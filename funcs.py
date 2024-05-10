from main import transcriber, Bot
import io
from aiogram.types import Voice
from pydub import AudioSegment

async def audio_to_text(file_path: str) -> str:
    """Принимает путь к аудио файлу, возвращает текст файла."""

    with open(file_path, "rb") as audio_file:
        transcript = transcriber.transcribe(audio_file)
    return transcript.text


async def save_voice_as_mp3(bot: Bot, voice: Voice) -> str:
    """Скачивает голосовое сообщение и сохраняет в формате mp3."""
    voice_file_info = await bot.get_file(voice.file_id)
    voice_ogg = io.BytesIO()
    await bot.download_file(voice_file_info.file_path, voice_ogg)
    voice_mp3_path = f"voice_files/voice-{voice.file_unique_id}.mp3"
    AudioSegment.from_file(voice_ogg, format="ogg").export(
        voice_mp3_path, format="mp3"
    )
    return voice_mp3_path

def temp_func(value:str)->str:
    return value
