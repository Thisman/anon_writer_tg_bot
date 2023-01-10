import sys

from aiogram import Bot, Dispatcher, executor, types

if(len(sys.argv) == 1):
    print('Не передан токен для авторизации')
    exit(1)

API_TOKEN = sys.argv[1]

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("""
Привет!
Я могу отправить анонимное сообщение в чат

Чтобы узнать как это сделать введи команду /help
Чтобы узнать больше информации введи команду /info
    """)

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("""
Чтобы отравить анонимное сообщение, напиши мне в формате CHAT_ID:MESSAGE

Если хочешь узнать ID чата, это можно сделать через @getidsbot
    """)

@dp.message_handler(commands=['info'])
async def help(message: types.Message):
    await message.reply("""
Автор: @tablescable
Ссылка на проект: https://github.com/Thisman/anon_writer_tg_bot
    """)

@dp.message_handler()
async def send_anon_message(message: types.Message):
    try:
        [chat_id, message_text] = message.text.split(':')
    except:
        await message.reply('Невалидный формат cообщения. Используйте число')
        return
    
    try:
        int(chat_id)
    except:
        await message.reply('Невалидный формат CHAT_ID.\nЧтобы узнать формат введи команду /help')
        return

    if(int(chat_id) >= 0):
        await message.reply('CHAT_ID должен быть меньше нуля. Возможно вы забыли добавить -?')
        return

    if(len(message_text) == 0):
        await message.reply('Вы пытаетесь отправить пустое сообщение')
        return

    await bot.send_message(chat_id, 'Аноним написал: ' + message_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
