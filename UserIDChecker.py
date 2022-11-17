from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='your token here')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await message.answer('your greeting message here')

@dp.message_handler(commands=['getuserid'])
async def getuserid(message: types.Message):
    await message.answer(f'userid received, thanks!\n\nYour userId: {message.from_user.id}')
    print(message.from_user.id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
