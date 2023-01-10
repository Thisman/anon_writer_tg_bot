from aiogram import Bot, Dispatcher, executor, types
import sys

if(len(sys.argv) == 1):
    print('No token pass')
    exit(1)

API_TOKEN = sys.argv[1]

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) #Явно указываем в декораторе, на какую команду реагируем. 
async def start(message: types.Message):
    await message.reply("Привет!\nЯ могу отправить анонимное сообщение в чат\nЧтобы узнать как это сделать введи команду /help") #Так как код работает асинхронно, то обязательно пишем await.

@dp.message_handler(commands=['help']) #Явно указываем в декораторе, на какую команду реагируем. 
async def help(message: types.Message):
    await message.reply("Чтобы отравить анонимное сообщение, напиши мне в формате CHAT_ID:MESSAGE") #Так как код работает асинхронно, то обязательно пишем await.

@dp.message_handler() #Создаём новое событие, которое запускается в ответ на любой текст, введённый пользователем.
async def send_anon_message(message: types.Message): #Создаём функцию с простой задачей — отправить обратно тот же текст, что ввёл пользователь.
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
