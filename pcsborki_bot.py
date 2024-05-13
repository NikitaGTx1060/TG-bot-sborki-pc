import telebot
from telebot import types

# Здесь нужно указать ваш токен от BotFather
TOKEN = '7140081152:AAG_eZYcuVJjMV58t974s-kzeFrreUgNAVY'

bot = telebot.TeleBot(TOKEN)

# Словарь с рекомендуемыми сборками ПК
recommendations = {
    'игровой': {
        'бюджетный': {'Название': 'Геймерский бюджетный', 'Характеристики': 'Процессор: AMD Ryzen 5, Видеокарта: NVIDIA GeForce GTX 1660, Оперативная память: 8 ГБ, Жесткий диск: 512 ГБ SSD', 'Цена': '$1000', 'Ссылка': 'link_to_product'},
        'средний': {'Название': 'Геймерский средний', 'Характеристики': 'Процессор: Intel Core i7, Видеокарта: NVIDIA GeForce RTX 2070, Оперативная память: 16 ГБ, Жесткий диск: 1 ТБ SSD', 'Цена': '$1500', 'Ссылка': 'link_to_product'},
        'премиум': {'Название': 'Геймерский премиум', 'Характеристики': 'Процессор: AMD Ryzen 9, Видеокарта: NVIDIA GeForce RTX 3080, Оперативная память: 32 ГБ, Жесткий диск: 2 ТБ NVMe SSD', 'Цена': '$2500', 'Ссылка': 'link_to_product'}
    },
    'офисный': {
        'бюджетный': {'Название': 'Офисный бюджетный', 'Характеристики': 'Процессор: Intel Core i3, Видеокарта: Встроенная, Оперативная память: 4 ГБ, Жесткий диск: 256 ГБ SSD', 'Цена': '$600', 'Ссылка': 'link_to_product'},
        'средний': {'Название': 'Офисный средний', 'Характеристики': 'Процессор: Intel Core i5, Видеокарта: Встроенная, Оперативная память: 8 ГБ, Жесткий диск: 512 ГБ SSD', 'Цена': '$800', 'Ссылка': 'link_to_product'},
        'премиум': {'Название': 'Офисный премиум', 'Характеристики': 'Процессор: Intel Core i7, Видеокарта: Встроенная, Оперативная память: 16 ГБ, Жесткий диск: 1 ТБ NVMe SSD', 'Цена': '$1200', 'Ссылка': 'link_to_product'}
    },
    'для 3D-моделирования': {
        'бюджетный': {'Название': 'Сборка для 3D-моделирования бюджетная', 'Характеристики': 'Процессор: AMD Ryzen 5, Видеокарта: NVIDIA GeForce GTX 1650, Оперативная память: 8 ГБ, Жесткий диск: 512 ГБ SSD', 'Цена': '$1200', 'Ссылка': 'link_to_product'},
        'средний': {'Название': 'Сборка для 3D-моделирования средняя', 'Характеристики': 'Процессор: AMD Ryzen 7, Видеокарта: NVIDIA GeForce RTX 2060, Оперативная память: 16 ГБ, Жесткий диск: 1 ТБ SSD', 'Цена': '$1800', 'Ссылка': 'link_to_product'},
        'премиум': {'Название': 'Сборка для 3D-моделирования премиум', 'Характеристики': 'Процессор: AMD Ryzen 9, Видеокарта: NVIDIA Quadro RTX 4000, Оперативная память: 32 ГБ, Жесткий диск: 2 ТБ NVMe SSD', 'Цена': '$3000', 'Ссылка': 'link_to_product'}
    }
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я могу помочь подобрать сборку ПК. Выберите тип ПК с помощью кнопок ниже.")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn1 = types.KeyboardButton('Игровой')
    itembtn2 = types.KeyboardButton('Офисный')
    itembtn3 = types.KeyboardButton('Для 3D-моделирования')
    markup.row(itembtn1, itembtn2)
    markup.row(itembtn3)

    bot.send_message(message.chat.id, "Выберите тип ПК:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Игровой' or message.text == 'Офисный' or message.text == 'Для 3D-моделирования':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Бюджетный')
        itembtn2 = types.KeyboardButton('Средний')
        itembtn3 = types.KeyboardButton('Премиум')
        markup.row(itembtn1, itembtn2)
        markup.row(itembtn3)

        bot.send_message(message.chat.id, "Выберите бюджет:", reply_markup=markup)
    else:
        bot.reply_to(message, "Извините, я не могу понять ваш запрос. Пожалуйста, выберите тип ПК с помощью кнопок.")

@bot.message_handler(func=lambda message: message.text in ['Бюджетный', 'Средний', 'Премиум'])
def handle_budget(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Отлично! Теперь выберите конкретную сборку:", reply_markup=markup)
    pc_type = message.text.lower()
    for key, value in recommendations.get(pc_type).items():
        bot.send_message(message.chat.id, f"Название ПК: {value['Название']}\\nКраткая характеристика: {value['Характеристики']}\\nЦена: {value['Цена']}\\nСсылка: {value['Ссылка']}")

@bot.message_handler(func=lambda message: message.text == '/back')
def back_message(message):
    send_welcome(message)

# Настройка вебхука
WEBHOOK_HOST = 'your_host'
WEBHOOK_PORT = 8443
WEBHOOK_LISTEN = '0.0.0.0'

WEBHOOK_SSL_CERT = './webhook_cert.pem'  # Путь к SSL-сертификату
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'  # Путь к закрытому SSL-ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (TOKEN)

# Установка вебхука и запуск бота
bot.remove_webhook()
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))