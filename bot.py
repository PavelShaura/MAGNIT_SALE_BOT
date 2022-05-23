import json
from aiogram import Bot, executor, types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink

from config import token

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Вперед за скидками!!!')
    start_buttons = ['Новомихайловский', 'Олгинка', 'Джубга', 'Лермонтово']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer('Где искать?', reply_markup=keyboard)


@dp.message_handler(Text(equals='Новомихайловский'))
async def novomix_city(message: types.Message):
    await message.answer('Ждите...')
    with open('Novomikhailovski.json', encoding="utf-8") as file:
        price = json.load(file)

    for k, v in sorted(price.items()):
        sales = f'{hbold(v["card_discount"])} 🥊\n\n' \
                f'{hbold(v["card_sale_date"])}\n\n' \
                f'{hlink(v["card_title_2"], v["card_img"])}\n\n' \
                f'Старая цена --  {v["card_old_price"]} руб.,\nНовая цена --  {hbold(v["card_price"])} руб.\n'

        await message.answer(sales)


@dp.message_handler(Text(equals='Олгинка'))
async def olginka_city(message: types.Message):
    await message.answer('Ждите...')
    with open('olginka.json', encoding="utf-8") as file:
        price = json.load(file)

    for k, v in sorted(price.items()):
        sales = f'{hbold(v["card_discount"])} 🥊\n\n' \
                f'{hbold(v["card_sale_date"])}\n\n' \
                f'{hlink(v["card_title_2"], v["card_img"])}\n\n' \
                f'Старая цена --  {v["card_old_price"]} руб.,\nНовая цена --  {hbold(v["card_price"])} руб.\n'

        await message.answer(sales)


@dp.message_handler(Text(equals='Джубга'))
async def dzhubga_city(message: types.Message):
    await message.answer('Ждите...')
    with open('Dzubga.json', encoding="utf-8") as file:
        price = json.load(file)

    for k, v in sorted(price.items())[-5:]:
        sales = f'{hbold(v["card_discount"])} 🥊\n\n' \
                f'{hbold(v["card_sale_date"])}\n\n' \
                f'{hlink(v["card_title_2"], v["card_img"])}\n\n' \
                f'Старая цена --  {v["card_old_price"]} руб.,\nНовая цена --  {hbold(v["card_price"])} руб.\n'

        await message.answer(sales)


@dp.message_handler(Text(equals='Лермонтово'))
async def lermontovo_city(message: types.Message):
    await message.answer('Ждите...')
    with open('Lermontovo.json', encoding="utf-8") as file:
        price = json.load(file)

    for k, v in sorted(price.items()):
        sales = f'{hbold(v["card_discount"])} 🥊\n\n' \
                f'{hbold(v["card_sale_date"])}\n\n' \
                f'{hlink(v["card_title_2"], v["card_img"])}\n\n' \
                f'Старая цена --  {v["card_old_price"]} руб.,\n Новая цена --  {hbold(v["card_price"])} руб.\n'

        await message.answer(sales)


if __name__ == '__main__':
    executor.start_polling(dp)
