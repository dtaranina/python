# NORMAL

# Задание-1:
# Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
# произвольными целыми цифрами, в результате в файле должно быть
# 2500-значное произвольное число.
# Найдите и выведите самую длинную последовательность одинаковых цифр
# в вышезаполненном файле.
# import random

import random

def get_numbers_to_file(qty):
    while True:
        rand_num = str(random.randrange(10))
        with open("data.txt", "a") as f:
            f.write(rand_num)
        with open("data.txt", "r", encoding="utf-8") as f:
            if len(f.read()) == qty:
                break
    with open("data.txt", "r", encoding="utf-8") as f:
        num = list(f.read())
    return num

def get_max_sequence(list):
    seq_dict = {}
    count = 0
    max = 0
    for i in range(10):
        for j in range(len(list) - 1):
            if str(i) == list[j] and list[j] == list[j + 1]:
                count += 1
            elif str(i) == list[j] and list[j] == list[j - 1]:
                count += 1
            else:
                if count > max:
                    max = count
                count = 0
        seq_dict.update([(i, max)])
        count = 0
    max_seq = ""
    for i in range(10):
        if len(str(i) * seq_dict[i]) > len(max_seq):
            max_seq = str(i) * seq_dict[i]
    return max_seq

print(get_max_sequence(get_numbers_to_file(2500)))


# Задание-2
# Сформировать квадратную матрицу, в каждой строке которой находится ровно один ноль на случайном месте, остальные
# элементы тоже рандомные. Пользователь вводит размер

matrix_size = int(input("Введите размер квадратной матрицы: "))

matrix = []
for k in range(matrix_size):
    matrix_row = []
    for i in range(matrix_size):
        j = random.randrange(2)
        matrix_row.append(j)
    if 0 not in matrix_row:
        rand_i = random.randrange(matrix_size - 1)
        matrix_row[rand_i] = 0
    elif 0 in matrix_row:
        while True:
            while matrix_row.count(0) > 1:
                matrix_row.remove(0)
                if matrix_row.count(0) == 1:
                    break
            if len(matrix_row) < matrix_size:
                for i in range(matrix_size - len(matrix_row)):
                    j = random.randrange(2)
                    matrix_row.append(j)
            elif matrix_row.count(0) == 1:
                break
    matrix.append(matrix_row)
print(matrix)

print(input("Нажмите Enter чтобы выйти: "))
