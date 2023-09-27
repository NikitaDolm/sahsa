import os

# Функция для регистрации новых студентов
def register():
    # Запрос данных у пользователя
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка, существует ли пользователь с таким логином
    if not is_user_exists(login):
        # Сохранение информации о новом студенте в файле "students.txt"
        with open("students.txt", "a") as file:
            file.write(f"{first_name} {last_name} {login} {password}\n")
        print("Регистрация успешно завершена.")
    else:
        print("Пользователь с таким логином уже существует.")

# Функция для проверки существования пользователя с данным логином
def is_user_exists(login):
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                if data[2] == login:
                    return True
    return False

# Функция для авторизации студентов
def login():
    # Запрос данных у пользователя
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    # Проверка, существует ли пользователь с таким логином и паролем
    if is_valid_credentials(login, password):
        print("Авторизация успешна.")
        # Здесь можно добавить функции, доступные авторизованным пользователям
    else:
        print("Неверные логин или пароль.")

# Функция для проверки логина и пароля
def is_valid_credentials(login, password):
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            for line in file:
                data = line.strip().split()
                if data[2] == login and data[3] == password:
                    return True
    return False

# Главное меню программы
while True:
    print("\n1. Регистрация")
    print("2. Авторизация")
    print("3. Выход")
    choice = input("Выберите опцию: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите 1, 2 или 3.")
