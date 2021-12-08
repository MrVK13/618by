from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import search as sr


bot = Bot(token='5001202520:AAHsLf1p0c9Mqyd4zOksEXXiqdCgda2Vibw', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

# cities = ['Минск', 'Светлогорск', 'Речица']
# cities_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
# cities_keyboard.add(*cities)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Введите станции отправки и назначения а так же дату\n(пример Минск Светлогорск 12.12.2021)')
       #message.answer(f'{message.from_user.id} Введите станции отправки и назначения а так же дату\n(пример Минск Светлогорск 12.12.2021)',)

@dp.message_handler()
async def zapr(message: types.Message):
    try:
        k = print(*sr.get_data(*message.text.split(' ')))
        await bot.send_message(message.from_user.id, *sr.get_data(*message.text.split(' ')))
    except:
        print('[WARNING] какая-то ошибка')



def main():
    executor.start_polling(dp)

if __name__ == '__main__':
    main()
