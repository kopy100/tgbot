import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7836943734:AAEi5VA5hNxpCFuJCCaWTv0k0cgRiKQcuFM'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

messages = [
    "Привет! Это сообщение номер 1",
    "Моды для Fabric:",  # Второе сообщение
    "Моды для Forge:",   # Третье сообщение
    "ТГК СЕРВЕРА",       # Четвёртое сообщение
    "Правила сервера",   # Пятое сообщение с кнопкой
    "Шестое сообщение на подходе",
    "Седьмое сообщение почти финал",
    "Восьмое и последнее сообщение"
]

keyboard_fabric = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Emotecraft", url="https://cdn.modrinth.com/data/pZ2wrerK/versions/oIYbvh6T/emotecraft-for-MC1.21.1-2.4.9-fabric.jar"),
        InlineKeyboardButton(text="Plasmovoice", url="https://cdn.modrinth.com/data/1bZhdhsH/versions/UCDHANKj/plasmovoice-fabric-1.21-2.1.3.jar"),
        InlineKeyboardButton(text="Customizable player models", url="https://cdn.modrinth.com/data/h1E7sQNL/versions/vaCTrzTl/CustomPlayerModels-Fabric-1.21-0.6.21a.jar"),
    ]
])

keyboard_forge = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Emotecraft (не поддерживается)", url="https://modrinth.com/"),
        InlineKeyboardButton(text="Plasmovoice", url="https://cdn.modrinth.com/data/1bZhdhsH/versions/8MQ7SfwO/plasmovoice-forge-1.21-2.1.3.jar"),
        InlineKeyboardButton(text="Customizable player models", url="https://cdn.modrinth.com/data/h1E7sQNL/versions/dyPU2OSD/CustomPlayerModelsLexForge-1.21-0.6.21a.jar"),
    ]
])

keyboard_tgk = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Нажми (ТГК)", url="https://t.me/fen1ixsCringeTeam")
    ]
])

keyboard_rules = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Открыть правила", url="https://t.me/fen1ixsCringeTeam/6")
    ]
])

@dp.message(Command("start"))
async def send_messages_sequence(message: types.Message):
    for idx, text in enumerate(messages):
        if idx == 1:
            await message.answer(text, reply_markup=keyboard_fabric)
        elif idx == 2:
            await message.answer(text, reply_markup=keyboard_forge)
        elif idx == 3:
            await message.answer(text, reply_markup=keyboard_tgk)
        elif idx == 4:
            await message.answer(text, reply_markup=keyboard_rules)
        else:
            await message.answer(text)
        await asyncio.sleep(1)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
