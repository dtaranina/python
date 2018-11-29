# EASY
# Для того, чтобы заработало надо раскомментить строки, начиная с 88


import os
import shutil


def make_dir(dir_name):
    """
    Создает папку dir_name в указанной директории
    """
    # склеивает текущую директорию и параметр dir_name
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        return f"\nУспешно создана папка {dir_name}"
    except FileExistsError:
        return f"\nНе удалось создать папку {dir_name}. Такая папка уже существует."


def del_dir(dir_path, dir_name):
    """
    Удаляет папку dir_name в директории dir_path
    """
    # склеивает текущую директорию и параметр dir_name
    upd_dir_path = os.path.join(dir_path, dir_name)
    try:
        shutil.rmtree(upd_dir_path, ignore_errors=True)
        return f"\nУспешно удалена папка {dir_name}"
    except FileNotFoundError:
        return f"\nНе удалось удалить папку {dir_name}. Такой папки не существует."


def show_all_dirs(dir_name):
    """
    Показывает все папки, которые находятся в директории dir_name
    """
    # создает список папок в директории dir_name
    dirs = []
    for obj in os.listdir(dir_name):
        if os.path.isdir(obj):
            dirs.append(obj)
    if len(dirs) > 0:
        return f"\nСписок папок в выбранной директории:\n{dirs}"
    else:
        return "\nНет папок в выбранной директории."


def show_all_files(dir_name):
    """
    Показывает все файлы, которые находятся в директории dir_name
    """
    # создает список файлов в директории dir_name
    files = []
    for file in os.listdir(dir_name):
        if os.path.isfile(file):
            files.append(file)
    if len(files) > 0:
        return f"\nСписок файлов в выбранной директории:\n{files}"
    else:
        return "\nНет файлов в выбранной директории."


def get_file_copy(dir_name, file_name):
    """
    Копирует файл file_name в директорию dir_name
    """
    # перебирает все объекты в папке dir_name
    for file in os.listdir(dir_name):
        # проверяет file_name на тип "файл"
        if os.path.isfile(file) and file_name == file:
            ext = os.path.splitext(file)
            shutil.copyfile(f"{dir_name}\{file}", f"{dir_name}\{ext[0]} - копия{ext[1]}")
            return f"\nУспешно создан файл {ext[0]} - копия{ext[1]}"
        else:
            return f"\nОшибка! {file_name} это папка. Введите имя существующего файла с расширением."
    else:
        return f"\nФайла {file_name} не существует. Введите имя существующего файла с расширением."


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


# qty = int(input("\nСколько папок вы хотите создать? "))
#
# for i in range(1, qty + 1):
#     print(make_dir(f"dir_{i}"))
#
# input("Нажмите Enter, чтобы удалить созданные папки")
#
# for i in range(1, qty + 1):
#     print(del_dir(f"dir_{i}"))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


# print(show_all_dirs(os.getcwd()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


# print(show_all_files(os.getcwd()))
# file_name = input("\nВведите имя файла с расширением, который нужно продублировать: ")
#
# print(get_file_copy(os.getcwd(), file_name))
