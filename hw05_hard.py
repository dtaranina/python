# HARD
# Для того, чтобы заработало надо закомментить строки в easy -  начиная с 88, в normal - 97


# Задание-1
#
# Написать программу для распаковки файлов в корневую из всех папок с расширениями (код взять с урока) и папки удалить

import os
import shutil
import hw05_easy
import hw05_normal


BASE_DIR = r"C:\Users\User\Desktop\Загрузки"
files = os.listdir(BASE_DIR)

extensions = set([os.path.splitext(file)[1] for file in files if os.path.isfile(os.path.join(BASE_DIR, file))])

for ext in extensions:
    if not os.path.exists(os.path.join(BASE_DIR, ext)):
        os.mkdir(os.path.join(BASE_DIR, ext))

for file in files:
    if os.path.isfile(os.path.join(BASE_DIR, file)):
        ext = os.path.splitext(file)[1]
        os.rename(os.path.join(BASE_DIR, file), os.path.join(BASE_DIR, ext, file))

input("Нажмите Enter, чтобы распаковать файлы из папок в корневую папки и затем удалить папки с расширениями ")

objects = os.listdir(BASE_DIR)
for obj in objects:
    if os.path.isdir(os.path.join(BASE_DIR, obj)):
        upd_dir_path = os.path.join(BASE_DIR, obj)
        os.chdir(upd_dir_path)
        for file in os.listdir(os.getcwd()):
            os.rename(os.path.join(upd_dir_path, file), os.path.join(BASE_DIR, file))
        try:
            os.chdir(BASE_DIR)
            shutil.rmtree(upd_dir_path, ignore_errors=True)
            print(f"\nУспешно удалена папка {obj}")
        except FileNotFoundError:
            print(f"\nНе удалось удалить папку {obj}. Такой папки не существует.")
