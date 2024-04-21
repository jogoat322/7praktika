import hashlib

def hash_password(password):
    # Хеширование пароля с использованием алгоритма MD5
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    return hashed_password

def list_users(cursor):
    query = "SELECT login FROM Users"
    cursor.execute(query)
    users = cursor.fetchall()
    print("Список пользователей:")
    for user in users:
        print(user[0])

def delete_user(connection, cursor):
    login = input("Введите логин пользователя, которого хотите удалить: ")
    query = "DELETE FROM Users WHERE login=?"
    cursor.execute(query, (login,))
    connection.commit()
    print("Пользователь с логином", login, "удален")

def add_user(connection, cursor):
    login = input("Введите логин нового пользователя: ")
    password = input("Введите пароль нового пользователя: ")
    user_type = int(input("Введите тип нового пользователя (1 - администратор, 2 - обычный пользователь): "))
    query = "INSERT INTO Users (login, password, utype_id) VALUES (?, ?, ?)"
    cursor.execute(query, (login, password, user_type))
    connection.commit()
    print("Новый пользователь добавлен")

def change_password(connection, cursor, user_id, new_password):
    query = "UPDATE Users SET password=? WHERE id=?"
    cursor.execute(query, (new_password, user_id))
    connection.commit()
    print("Пароль успешно изменен")

def admin_menu(connection, cursor, user_id):
    while True:
        print("\nМеню администратора:")
        print("1. Вывести список пользователей")
        print("2. Удалить пользователя")
        print("3. Добавить нового пользователя")
        print("4. Сменить свой пароль")
        print("5. Выйти из учетной записи")

        choice = input("Выберите действие: ")

        if choice == "1":
            list_users(cursor)
        elif choice == "2":
            delete_user(connection, cursor)
        elif choice == "3":
            add_user(connection, cursor)
        elif choice == "4":
            new_password = input("Введите новый пароль: ")
            change_password(connection, cursor, user_id, new_password)
        elif choice == "5":
            print("Выход из учетной записи")
            break
        else:
            print("Некорректный ввод")

def user_menu(connection, cursor, user_id):
    while True:
        print("\nМеню пользователя:")
        print("1. Сменить свой пароль")
        print("2. Захешировать свой пароль")
        print("3. Выйти из учетной записи")

        choice = input("Выберите действие: ")

        if choice == "1":
            new_password = input("Введите новый пароль: ")
            change_password(connection, cursor, user_id, new_password)
        elif choice == "2":
            password = input("Введите текущий пароль: ")
            hashed_password = hash_password(password)
            change_password(connection, cursor, user_id, hashed_password)
        elif choice == "3":
            print("Выход из учетной записи")
            break
        else:
            print("Некорректный ввод")

def register_user(connection, cursor):
    login = input("Введите логин нового пользователя: ")
    password = input("Введите пароль нового пользователя: ")
    user_type = int(input("Введите тип нового пользователя (1 - администратор, 2 - обычный пользователь): "))
    query = "INSERT INTO Users (login, password, utype_id) VALUES (?, ?, ?)"
    cursor.execute(query, (login, password, user_type))
    connection.commit()
    print("Новый пользователь зарегистрирован")

def identify_by_login(connection, cursor):
    login = input("Введите логин: ")

    query = "SELECT id, utype_id FROM Users WHERE login=?"
    cursor.execute(query, (login,))
    user = cursor.fetchone()

    if user:
        return True
    else:
        return False

def authenticate_user(connection, cursor):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    query = "SELECT id, utype_id FROM Users WHERE login=? AND password=?"
    cursor.execute(query, (login, password))
    user = cursor.fetchone()

    if user:
        user_id, user_type = user[0], user[1]
        if user_type == 1:
            print("Вы авторизованы с правами администратора.")
            admin_menu(connection, cursor, user_id)
        elif user_type == 2:
            print("Вы авторизованы с правами пользователя")
            user_menu(connection, cursor, user_id)
    else:
        print("Неправильный логин или пароль")