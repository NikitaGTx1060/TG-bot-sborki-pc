from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
from database import add_user, get_user, close_connection

# Токен вашего бота
TOKEN = "7053415356:AAHM8P3TU3IneM8xNnQc9N4no9DQTm99q4M"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    add_user(user_id, username, first_name, last_name)

    await message.answer("Привет! Я твой новый бот.")

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
