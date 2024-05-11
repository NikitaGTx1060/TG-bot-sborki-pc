import telebot
from telebot import types

bot = telebot.TeleBot("7140081152:AAG_eZYcuVJjMV58t974s-kzeFrreUgNAVY")

# Step 1: Greeting and introduction
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Игровой', 'Офисный', 'Для 3D моделирования', 'Для дизайна')
    bot.send_message(message.chat.id, "Привет! Я бот помощник в подборе сборки ПК. Укажи свой бюджет и требования, и я подскажу тебе лучший вариант.", reply_markup=markup)

# Step 2: Selecting PC type
@bot.message_handler(func=lambda message: message.text in ['Игровой', 'Офисный', 'Для 3D моделирования', 'Для дизайна'])
def select_pc_type(message):
    pc_type = message.text
    budget_options = {
        'Игровой': ['до 40000 тысяч рублей', 'до 60000 тысяч рублей', 'до 70000 тысяч рублей', 'до 90000 тысяч рублей', 'до 100000 и более тысяч рублей'],
        'Офисный': ['до 20000 тысяч рублей', 'до 30000 тысяч рублей', 'до 40000 тысяч рублей'],
        'Для 3D-моделирования, Для дизайна': ['до 180000 тысяч рублей', 'до 230000 тысяч рублей'],
        'Для дизайна': ['до 180000 тысяч рублей', 'до 230000 тысяч рублей']
    }
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for budget in budget_options[pc_type]:
        markup.row(budget)
    bot.send_message(message.chat.id, f"Выберите бюджет для {pc_type} ПК:", reply_markup=markup)

# Step 3: Selecting budget
@bot.message_handler(func=lambda message: message.text in ['до 20000 тысяч рублей', 'до 30000 тысяч рублей', 'до 40000 тысяч рублей', 'до 60000 тысяч рублей', 'до 70000 тысяч рублей', 'до 90000 тысяч рублей', 'до 100000 и более тысяч рублей', 'до 180000 тысяч рублей', 'до 230000 тысяч рублей'])
def select_budget(message):
    budget = message.text
    pc_builds = get_pc_builds(budget)  # Replace this function with your own implementation
    send_pc_builds(message.chat.id, pc_builds)

def get_pc_builds(budget):
    # Replace this function with your own implementation to fetch PC builds
    # Return a list of dictionaries, where each dictionary represents a PC build
    # Each dictionary should have keys: 'name', 'description', 'price', and 'link'
    return [
        {
            'name': 'PC Build 1',
            'description': 'Игровая сборка на бюджет до 60000 рублей',
            'price': '55000 рублей',
            'link': 'https://example.com/pc-build-1'
        },
        {
            'name': 'PC Build 2',
            'description': 'Офисная сборка на бюджет до 30000 рублей',
            'price': '25000 рублей',
            'link': 'https://example.com/pc-build-2'
        },
        # Add more PC builds as needed
    ]

def send_pc_builds(chat_id, pc_builds):
    for pc_build in pc_builds:
        text = f"Название ПК: {pc_build['name']}\n" \
               f"Краткая характеристика: {pc_build['description']}\n" \
               f"Цена: {pc_build['price']}\n" \
               f"Ссылка: {pc_build['link']}"
        bot.send_message(chat_id, text)

bot.polling()