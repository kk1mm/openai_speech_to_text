import logging
#hello
from AI_TOKEN import BOT_TOKEN, TOKEN1
import asyncio


from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message



import assemblyai as aai

from funcs import *
aai.settings.api_key = TOKEN1

router: Router = Router()
logging.basicConfig(level=logging.INFO)
config = aai.TranscriptionConfig(language_code="uk", dual_channel=True)
transcriber = aai.Transcriber(config=config)

MALYSHKA = [1,2]


@router.message(F.content_type == "voice")
async def process_voice_message(message: Message, bot: Bot):
    """Принимает все голосовые сообщения и транскрибирует их в текст."""
    voice_path = await save_voice_as_mp3(bot, message.voice)
    transcripted_voice_text = await audio_to_text(voice_path)

    if transcripted_voice_text:
        await message.reply(text=transcripted_voice_text)


@router.message(F.content_type != "voice")
async def not_voice(message: Message, bot: Bot):
    await message.reply(text='Send an audio pls 8:')


async def main():
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
