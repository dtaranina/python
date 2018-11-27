# NORMAL

# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    """
    Возвращает ряд Фибоначчи от и до заданного числа
    """
    if n < m:                                                           # проверяем введены ли корректные аргументы
        fibonacci = [1, m]
        i = 0
        while fibonacci[-2] < fibonacci[-1]:                            # находим последнее число в ряде
            if i == 0:
                fibonacci.insert(-1, fibonacci[i])
            else:
                fibonacci.insert(-1, fibonacci[i] + fibonacci[i - 1])
            i += 1
        if fibonacci[-2] == fibonacci[-1]:
            fibonacci.pop(-2)
        elif fibonacci[-2] > fibonacci[-1]:
            fibonacci.pop(-2)
            fibonacci.pop(-1)
        i = 0
        while True:                                                     # находим первое числа в ряде
            if fibonacci[i] <= n <= fibonacci[i + 1]:
                fibonacci = fibonacci[i + 1:]
                break
            i += 1
        return fibonacci
    else:
        return f"\nАргументы {n} и {m} заданы неверно"

n = int(input("\nВведите начальное числа ряда Фибоначчи: "))
m = int(input("\nВведите конечное число ряда Фибоначчи: "))

print(fibonacci(n, m))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    while True:
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list.insert(i + 2, origin_list[i])
                origin_list.pop(i)
        check = 0
        for i in range(len(origin_list) - 1):
            if origin_list[i] <= origin_list[i + 1]:
                check += 1
        if check == len(origin_list) - 1:
            break
    return origin_list

print("\nОтсортированный массив: \n")
print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))
