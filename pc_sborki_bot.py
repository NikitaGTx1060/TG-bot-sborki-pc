import telebot
from telebot import types

# Здесь нужно указать ваш токен от BotFather
TOKEN = '7140081152:AAG_eZYcuVJjMV58t974s-kzeFrreUgNAVY'

bot = telebot.TeleBot(TOKEN)

# Словарь с рекомендуемыми сборками ПК
recommendations = {
    'игровой': {
        'бюджетный': {'Название': 'ПК ARDOR GAMING NEO M144', 'Характеристики': 'Intel Core i3-12100F, Intel H610, 4 x 3.3 ГГц, 16 ГБ DDR4, GeForce GTX 1650, SSD 500 ГБ, без ОС', 'Цена': '49 499 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/5b8f00a276f0ed20/pk-ardor-gaming-neo-m144/'},
        'средний': {'Название': 'ПК ARDOR GAMING NEO M143', 'Характеристики': 'Intel Core i5-12400F, Intel H610, 6 x 2.5 ГГц, 16 ГБ DDR4, GeForce RTX 3050, SSD 1000 ГБ, без ОС ', 'Цена': '68 299 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/3aebe86e61cbed20/pk-ardor-gaming-neo-m143/'},
        'премиум': {'Название': 'ПК ARDOR GAMING RAGE H332', 'Характеристики': 'Intel Core i5-13400F, Intel B760, 6 x 2.5 ГГц, 32 ГБ DDR5, GeForce RTX 4060 Ti, SSD 1500 ГБ, без ОС', 'Цена': '124 499 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/3c7723e9fd4ad582/pk-ardor-gaming-rage-h332/'}
    },
    'офисный': {
        'бюджетный': {'Название': 'ПК DEXP Atlas H418', 'Характеристики': 'Intel Core i3-12100, Intel H610, 4 x 3.3 ГГц, 8 ГБ DDR4, SSD 500 ГБ, без ОС', 'Цена': '28 999 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/c9ce4dcd785fed20/pk-dexp-atlas-h418/'},
        'средний': {'Название': 'ПК DEXP Atlas H436', 'Характеристики': 'AMD Ryzen 7 5700G, AMD B550, AMD B550, 8 x 3.8 ГГц, 16 ГБ DDR4, SSD 500 ГБ, без ОС', 'Цена': '39 799 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/ed983f6dd5e1ed20/pk-dexp-atlas-h436/'},
        'премиум': {'Название': 'ПК DEXP Atlas H399', 'Характеристики': 'Intel Core i7-12700, Intel H610, 8 x 2.1 ГГц, 16 ГБ DDR4, SSD 512 ГБ, без ОС', 'Цена': '46 799 ₽', 'Ссылка': 'https://www.dns-shop.ru/product/185bdfd41707ed20/pk-dexp-atlas-h399/'}
    },
    'для 3D-моделирования': {
        'бюджетный': {'Название': 'G1 PRO MAX', 'Характеристики': 'Intel® Core™ i5-13400(F), MSI PRO B760M-A, Palit GeForce RTX 4060 Dual, 16GB Kingston FURY Beast RGB, 500GB ADATA LEGEND 800', 'Цена': '159 500 ₽', 'Ссылка': 'https://hyperpc.ru/workstation/g1-pro/max'},
        'средний': {'Название': 'G1 PRO ULTRA', 'Характеристики': 'Intel® Core™ i5-14500, MSI PRO B760M-A, Palit GeForce RTX 4060 Dual, 32GB Kingston FURY Beast RGB, 500GB ADATA LEGEND 800', 'Цена': '179 800 ₽', 'Ссылка': 'https://hyperpc.ru/workstation/g1-pro/ultra'},
        'премиум': {'Название': 'LUMEN PRO', 'Характеристики': 'Palit GeForce RTX 4060 Ti Dual, Intel® Core™ i5-13400(F), MSI MAG B760 TOMAHAWK, 32GB TEAMGROUP T-Force Delta RGB Black, 1TB Samsung 970 EVO Plus', 'Цена': '227 700 ₽', 'Ссылка': 'https://hyperpc.ru/workstation/lumen-pro/base'}
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