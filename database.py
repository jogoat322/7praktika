import sqlite3

def connect_to_database(database_name):
    try:
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        print("Подключение к базе данных успешно установлено")
        return connection, cursor
    except sqlite3.Error as error:
        print("Ошибка при подключении к базе данных:", error)

