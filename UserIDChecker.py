from aiogram import Bot, Dispatcher, executor, types

import config as config

bot = Bot(token=config.test_token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await message.answer('Никите нужно получить ваши userId, чтобы к админ-боту имели доступ только вы и он')

@dp.message_handler(commands=['getuserid'])
async def getuserid(message: types.Message):
    await message.answer('userid получен, спасибо Макс или Настя!')
    user_id = message.from_user.id
    print(user_id)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)