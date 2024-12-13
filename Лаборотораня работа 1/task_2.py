from task_1 import (Table, Tree, User)

if __name__ == "__main__":
    # Создание объектов для всех классов
    try:
        table = Table(2.0, 1.5, "Wood")
        tree = Tree("Oak", 10.0, 50)
        user = User("JohnDoe", "john@example.com", 25)


    except ValueError as e:
        print('Ошибка: неправильные данные')

    # Проверка методов с некорректными аргументами

    try:
        # Попытка создания стола с некорректными размерами
        invalid_table = Table(-1.0, 1.5, "Wood")  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания дерева с пустым названием
        invalid_tree = Tree("", 10.0, 50)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')

    try:
        # Попытка создания пользователя с некорректными данными
        invalid_user = User("", "invalidemail", -5)  # Некорректный аргумент
    except ValueError as e:
        print('Ошибка: неправильные данные')
