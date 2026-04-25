import dateparser
from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from holiday_service import get_holidays_for_date

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "👋 Привет! Я бот для поиска праздников.\n"
        "Просто отправь мне любую дату, например:\n"
        "• 1 января\n• 8 марта\n• 23 февраля\n"
        "• завтра\n• через неделю\n• 25.12.2025"
    )

@router.message(F.text)
async def handle_date_input(message: Message):
    user_input = message.text.strip()
    
    # Парсим дату из естественного языка
    parsed_date = dateparser.parse(
        user_input,
        languages=['ru'],           # русский язык
        settings={'PREFER_DATES_FROM': 'future'}  # будущие даты в приоритете
    )
    
    if not parsed_date:
        await message.answer(
            "❌ Не удалось распознать дату. Попробуйте ещё раз, например: '1 января' или '25.12.2025'."
        )
        return
    
    # Ищем праздники
    holidays_list = get_holidays_for_date(parsed_date.date(), country="RU")
    
    # Формируем ответ
    date_str = parsed_date.strftime("%d.%m.%Y")
    if holidays_list:
        holidays_text = "\n".join(f"• {h}" for h in holidays_list)
        response = f"🎉 Праздники на {date_str}:\n{holidays_text}"
    else:
        response = f"📅 На {date_str} нет официальных праздников в России."
    
    await message.answer(response)