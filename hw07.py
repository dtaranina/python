#!/usr/bin/python3

# == Лото ==
# Правила игры в лото.
# Игра ведется с помощью специальных карточек, на которых отмечены числа,
# и фишек (бочонков) с цифрами.
# Количество бочонков — 90 штук (с цифрами от 1 до 90).
# Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
# расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
# --------------------------
#     9 43 62          74 90
#  2    27    75 78    82
#    41 56 63     76      86
# --------------------------
# В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
# случайная карточка.
# Каждый ход выбирается один случайный бочонок и выводится на экран.
# Также выводятся карточка игрока и карточка компьютера.
# Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
# Если игрок выбрал "зачеркнуть":
# 	Если цифра есть на карточке - она зачеркивается и игра продолжается.
# 	Если цифры на карточке нет - игрок проигрывает и игра завершается.
# Если игрок выбрал "продолжить":
# 	Если цифра есть на карточке - игрок проигрывает и игра завершается.
# 	Если цифры на карточке нет - игра продолжается.
#
# Побеждает тот, кто первый закроет все числа на своей карточке.
# Пример одного хода:
# Новый бочонок: 70 (осталось 76)
# ------ Ваша карточка -----
#  6  7          49    57 58
#    14 26     -    78    85
# 23 33    38    48    71
# --------------------------
# -- Карточка компьютера ---
#  7 11     - 14    87
#       16 49    55 77    88
#    15 20     -       76  -
# --------------------------
# Зачеркнуть цифру? (y/n)
# Подсказка: каждый следующий случайный бочонок из мешка удобно получать
# с помощью функции-генератора.
# Подсказка: для работы с псевдослучайными числами удобно использовать
# модуль random: http://docs.python.org/3/library/random.html


# создать класс карточка
# генерить внутри него рандомное заполнение поля X на Y
# создать класс по обертыванию карточек
# в начале игры вызывать 2 объекта из этого класса
# создать метод по зачеркиванию числа?
# сделать проверку на "зачеркнуть" и "продолжить"

# создать класс бочонок?
# его работа - генерить случайное число от 1 до 90 до 90 раз, при этом исключая
# число всякий раз, как оно будет появляться

# т. к. это консольная игра, то надо печатать карточку всякий раз, как будет
# появляться бочонок

from random import randint


class Card:
    def __init__(self, lines_number, columns_number, first_number, last_number, number_of_emptys):
        self.lines_number = lines_number
        self.columns_number = columns_number
        self.first_number = first_number
        self.last_number = last_number
        self.number_of_emptys = number_of_emptys

        if self.columns_number < number_of_emptys:
            print("Количество пустых клеток должно быть меньше, чем количество столбцов")
            exit(0)
        elif self.columns_number <= 2:
            print("Количество столбцов должно быть больше двух")
            exit(1)
        elif self.lines_number * self.columns_number > (self.last_number - self.first_number):
            print("Диапазон чисел должен быть больше или равен произедению строка*столбец")
            exit(2)

    def create_lines(self):
        lines = []
        for i in range(self.lines_number):
            lines.append(list())

        while True:
            num = randint(self.first_number, self.last_number)
            count = 0
            for i, line in enumerate(lines):
                if num in lines[i]:
                    count += 1
            if count == 0:
                for i, line in enumerate(lines):
                    if len(lines[self.lines_number - 1]) != self.columns_number:
                        lines[self.lines_number - 1].append(num)
                        break
                    else:
                        self.lines_number -= 1
                if self.lines_number < 0:
                    break

        for line in lines:
            for i in range(self.number_of_emptys):
                while True:
                    empty_el = randint(0, self.columns_number - 1)
                    if line[empty_el] is not None:
                        line.insert(empty_el, None)
                        line.pop(empty_el + 1)
                        break

        for line in lines:
            card_line = ""
            for i in line:
                if i is not None and i < 10:
                    card_line += f" {i} "
                elif i is None:
                    card_line += f"   "
                else:
                    card_line += f"{i} "
            print(card_line)
        return ""


card1 = Card(3, 9, 1, 90, 4)

print(Card.create_lines(card1))
