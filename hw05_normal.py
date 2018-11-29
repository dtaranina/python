# NORMAL
# Для того, чтобы заработало надо раскомментить строку 97


# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть указанной папки
# 3. Удалить папку
# 4. Создать папку
# При выборе любых пунктов печатается статус "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import hw05_easy
import os


def return_back(base_dir):
    """
    Переходит назад в предыдущую папку, если рабочая папка не корневая
    """
    # проверка на некорневую папку
    if os.getcwd() != base_dir:
        # разбивает путь на кортеж ("голова", "хвост")
        dir_path = os.path.split(os.getcwd())
        # переходит в папку "голова"
        os.chdir(dir_path[0])
        return f"\nУспешный переход в папку {dir_path[0]}"
    else:
        return "\nВы находитесь в корневой директории. Назад перейти невозможно"


def change_dir(base_dir, dir_name):
    """
    Переходит в одну из папок в рабочей папке
    """
    # склеивает текущую директорию и параметр dir_name
    dir_path = os.path.join(base_dir, dir_name)
    try:
        os.chdir(dir_path)
        return f"\nУспешный переход в папку {dir_name}\nТекущая директория: {os.getcwd()}"
    except FileNotFoundError:
        return f'\nНевозможно перейти в папку {dir_name}. Такой папки не существует.'


BASE_DIR = os.getcwd()

def console_menu():
    while True:
        print("""
Консольное меню

1. Перейти в папку
2. Просмотр указанной папки
3. Удалить папку
4. Создать папку
5. Выйти из консольного меню
        """)

        do = int(input("Выберите действие: "))

        if do == 1:
            print(hw05_easy.show_all_dirs(os.getcwd()))
            question_for_back = input("\nВернуться в предыдущую папку? [Y/N] ")
            question_for_back.lower()
            if question_for_back == "y":
                print(return_back(BASE_DIR))
            else:
                dir_name = input("\nВведите имя папки, в которую хотите перейти: ")
                print(change_dir(os.getcwd(), dir_name))

        elif do == 2:
            print(hw05_easy.show_all_dirs(os.getcwd()))
            print(hw05_easy.show_all_files(os.getcwd()))

        elif do == 3:
            print(hw05_easy.show_all_dirs(os.getcwd()))
            dir_name = input("\nВведите имя папки, которую хотите удалить: ")
            print(hw05_easy.del_dir(os.getcwd(), dir_name))

        elif do == 4:
            dir_name = input("\nВведите имя папки, которую хотите создать: ")
            print(hw05_easy.make_dir(dir_name))

        elif do == 5:
            print("Успешный выход из консольного меню.")
            break

        else:
            if do != range(1, 5):
                print("Действие не найдено. Попробуйте еще раз.")


console_menu()
