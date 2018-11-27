# EASY

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """
    округляет полученное десятичное число до требуемого кол-ва знаков после запятой
    """
    if type(number) is float and type(ndigits) is int:                      # проверяем введены ли корректные аргументы
        number_go_to_string = str(number)                                   # преобразовываем десятичное число в строку
        split = number_go_to_string.split(".")                              # разбиваем строку по разделителю "."
        left_part = split[0]                                                # запихиваем левую часть в переменную
        right_part = int(split[1][0:ndigits + 1])                       # правую часть в int и в запихиваем в переменную
        if right_part % 10 > 5:                                             # математическое округление
            right_part += 10
            if len(str(right_part)) > len(split[1][0:ndigits + 1]):         # проверяем увеличилась ли правая часть
                right_part = 0
                left_part = str(int(split[0]) + 1)
        right_part = str(right_part)
        round_number = float(f"{left_part}.{right_part[0:ndigits]}")        # объединяем и преобразовываем в float
        return round_number
    else:
        return f"Аргументы {number} и {ndigits} введены неверно. Пожалуйста, укажите корректные аргументы"

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    """
    Проверяет счастливый ли выпал билет
    """
    if type(ticket_number) is int:                              # проверяем введены ли корректные аргументы
        print(f"\nРезультат проверки числа {ticket_number}:")
        number_list = []
        while ticket_number > 0:                                # делаем из числа массив
            number_list.append(ticket_number % 10)
            ticket_number //= 10
        if len(number_list) % 2 == 0:                           # проверка на четное кол-во чисел
            sum1 = 0
            sum2 = 0
            for i in range(int(len(number_list) / 2)):          # складываем первые и последние числа
                sum1 += number_list[-i - 1]
                sum2 += number_list[i]
            print(f"\nСумма первых чисел: {sum1}\nСумма последних чисел: {sum2}\n")
            if sum1 == sum2:
                return "Билет счастливый :)"
            elif sum1 != sum2:
                return "Билет не счастливый :("
        else:
            return "\nНе могу посчитать суммы чисел, т. к. их нечетное количество"
    else:
        return "\nАргумент должен быть целым числом"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(436.751))
print(lucky_ticket("436751"))