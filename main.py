from database import *
from func import *

database_name = "base2.db"
connection, cursor = connect_to_database(database_name)

if connection:
    while True:
            print("\nГлавное меню:")
            print("1. Войти")
            print("2. Зарегистрироваться")
            print("3. Идентификация по логину")
            print("4. Выход")

            choice = input("Выберите действие: ")

            if choice == "1":
                authenticate_user(connection, cursor)
            elif choice == "2":
                register_user(connection, cursor)
            elif choice == "3":
                if identify_by_login(connection, cursor):
                    print("Пользователь с таким логином существует")
                else:
                    print("Пользователь с таким логином не существует")
            elif choice == "4":
                print("Выход из программы")
                break
            else:
                print("Некорректный ввод")

    connection.close()
    print("Соединение с базой данных закрыто")

