import sqlite3

# Подключение к базе данных SQLite3
conn = sqlite3.connect('bot_database.db')
cursor = conn.cursor()

# Создание таблицы для хранения данных
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT
    )
''')

# Функция для добавления пользователя в базу данных
def add_user(user_id, username, first_name, last_name):
    cursor.execute('INSERT INTO users (id, username, first_name, last_name) VALUES (?, ?, ?, ?)',
                   (user_id, username, first_name, last_name))
    conn.commit()

# Функция для получения пользователя из базы данных по ID
def get_user(user_id):
    cursor.execute('SELECT * FROM users WHERE id=?', (user_id,))
    return cursor.fetchone()

# Закрытие соединения с базой данных
def close_connection():
    conn.close()
