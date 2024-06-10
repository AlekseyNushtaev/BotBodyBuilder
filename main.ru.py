import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "7116078329:AAGG8qn7lhYwtNjF1AWvntIL6ikd6AMHlEk"
MY_ID = 1764521892

dp = Dispatcher()
bot = Bot(token=TOKEN)

builder = InlineKeyboardBuilder()

builder.row(InlineKeyboardButton(text="Консультация 🧑‍💻", url="https://t.me/moskowcev"))
builder.row(InlineKeyboardButton(text="Наш ламповый чатик 🥰 ", url="https://t.me/+wTpmtGIYoXY0M2My"))
builder.row(InlineKeyboardButton(text="Мой канал ✈️", url="https://t.me/moskovcev1"))
builder.row(InlineKeyboardButton(text="Отзывы обо мне ✅", url="https://t.me/moskovcev1/53"))
builder.row(InlineKeyboardButton(text="Ещё обо мне 📘", url="https://t.me/moskovcev1/47"))
builder.row(
    InlineKeyboardButton(text="Я в ВК 🔵", url="https://vk.com/be_strong_and_happy"),
    InlineKeyboardButton(text="Я в YouTube 🔴", url="https://www.youtube.com/@Miha9972")
)

main_keyboard_markup = builder.as_markup()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    welcome_text = f"""
Привет, {message.from_user.full_name}!🌟

Ищешь тренера, который преобразит твои тренировки? Ты нашел меня!

Вот кратко о моем опыте и достижениях:

🏆 Учился у лучшего бодибилдера России 2019 года.
🥇 Чемпион Восточной Европы по бодибилдингу и фитнесу 2017 года.
🎗 Лучший тренер крупнейших фитнес-центров Петербурга (2016-2018).
🧘‍♂️ Обучение у мастеров Бали.
🏅 Помог более 1000 клиентов достигнуть их целей.
🏅 Опыт в самбо – 5 лет, в спортзале – 16 лет.

Моя методика нацелена на достижение результатов без изнурительных диет. Подход адаптирован под твои потребности и график. Провожу занятия как онлайн, так и офлайн.

С нетерпением жду нашего сотрудничества! 🔥
"""
    await message.answer_video(
        FSInputFile("video.mp4"),
        caption=welcome_text,
        reply_markup=main_keyboard_markup
    )
    await bot.send_message(
        chat_id=MY_ID,
        text=f"Пользователь @{message.from_user.username} нажал на кнопку Start")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())