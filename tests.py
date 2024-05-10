import pytest
from unittest.mock import MagicMock, patch
from aiogram import types
from main import process_voice_message, not_voice,audio_to_text, save_voice_as_mp3



@pytest.fixture
def bot():
    return MagicMock()


@pytest.mark.asyncio
async def test_process_voice_message(bot):
    # Przygotowanie danych wejściowych
    voice_message = types.Voice(file_id="test_file_id")
    message = MagicMock()
    message.voice = voice_message

    # Mockowanie funkcji audio_to_text
    with patch("funcs.audio_to_text") as mock_audio_to_text:
        mock_audio_to_text.return_value = "Testowa wiadomość transkrybowana"

        # Wywołanie funkcji do przetwarzania wiadomości głosowej
        await process_voice_message(message, bot)

        # Sprawdzenie czy odpowiedź została wysłana
        message.reply.assert_called_once_with(text="Testowa wiadomość transkrybowana")


@pytest.mark.asyncio
async def test_not_voice(bot):
    # Przygotowanie danych wejściowych
    message = MagicMock()

    # Wywołanie funkcji dla niegłosowej wiadomości
    await not_voice(message, bot)

    # Sprawdzenie czy odpowiednia wiadomość została wysłana
    message.reply.assert_called_once_with(text='Send an audio pls 8:')


@pytest.mark.asyncio
async def test_audio_to_text():
    # Testowanie funkcji audio_to_text
    file_path = "test_voice.mp3"
    expected_text = "Testowa transkrypcja"

    # Symulacja przekształcenia pliku audio na tekst
    result = await audio_to_text(file_path)

    # Sprawdzenie czy otrzymany tekst jest zgodny z oczekiwanym
    assert result == expected_text


@pytest.mark.asyncio
async def test_save_voice_as_mp3(bot):
    # Testowanie funkcji save_voice_as_mp3
    voice_file = types.Voice(file_id="test_file_id")
    expected_file_path = "voice_files/voice-test_file_id.mp3"

    # Symulacja zapisania pliku audio
    with patch("main.AudioSegment") as mock_audio_segment:
        mock_audio_segment.from_file.return_value = mock_audio_segment
        mock_audio_segment.export.return_value = None

        result = await save_voice_as_mp3(bot, voice_file)

    # Sprawdzenie czy otrzymany ścieżka pliku jest zgodna z oczekiwaną
    assert result == expected_file_path
