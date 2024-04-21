import os
import sqlite3

DB_PATH = 'base2.db'

# удаление файла базы данных
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

# ВНИМАНИЕ: потоконебезопасный вариант

# Пример 1. Подключение к базе
try:
    connection = sqlite3.connect(DB_PATH) # выполняется подключение к базе данных
    cursor = connection.cursor() # позволяет выполнять SQLite-запросы
    print("База данных создана и успешно подключена к SQLite")
    cursor.close() # закрываем курсор

except sqlite3.Error as error: # можно обработать любую ошибку и исключение
    print("Ошибка при подключении к sqlite", error)
finally:
    if connection:
        connection.close() # закрываем соединение
        print("Соединение с SQLite закрыто")

# Пример 2. Создание таблиц и их заполнение
try:
    connection = sqlite3.connect(DB_PATH) # выполняется подключение к базе данных
    cursor = connection.cursor() # позволяет выполнять SQLite-запросы
    print("База данных создана и успешно подключена к SQLite")

    # создание таблицы User_types
    CREATE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS User_types (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                utype TEXT NOT NULL UNIQUE);'''
    cursor.execute(CREATE_TABLE_QUERY) # выполнить запрос в базу данных
    connection.commit() # сохранить изменение
    print("Таблица User_types создана")

    # создание таблицы Users
    CREATE_TABLE_QUERY = '''CREATE TABLE IF NOT EXISTS Users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                login TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL UNIQUE,
                                utype_id INTEGER,
                                FOREIGN KEY (utype_id) REFERENCES User_types(id) 
                                ON DELETE CASCADE);'''
    cursor.execute(CREATE_TABLE_QUERY) # выполнить запрос в базу данных
    connection.commit() # сохранить изменение
    print("Таблица Users создана")

    # заполнение нескольких строк
    records = [('Администратор',),
               ('Пользователь',)]
    INSERT_QUERY = """INSERT INTO User_types (utype) VALUES (?);"""
    cursor.executemany(INSERT_QUERY, records)
    connection.commit() # сохранить изменение
    print("Таблица User_types заполнена")

    # внесение одной записи
    LOGIN = 'admin'
    PASSWORD = 'admin'
    UTYPE_ID = 1
    INSERT_QUERY = """INSERT INTO Users (login, password, utype_id) VALUES (?,?,?);"""
    cursor.execute(INSERT_QUERY, (LOGIN, PASSWORD, UTYPE_ID))
    connection.commit() # сохранить изменение
    print("Таблица Users заполнена")

    # заполнение нескольких строк
    records = [('ivan','123',2),
               ('petr','456',2),
               ('pavel','789',2)]
    INSERT_QUERY = """INSERT INTO Users (login, password, utype_id) VALUES (?,?,?);"""
    cursor.executemany(INSERT_QUERY, records)
    connection.commit() # сохранить изменение
    print("Таблица Users заполнена")

    cursor.close() # закрываем курсор

except sqlite3.Error as error: # можно обработать любую ошибку и исключение
    print("Ошибка при подключении к sqlite", error)
finally:
    if connection:
        connection.close() # закрываем соединение
        print("Соединение с SQLite закрыто")

