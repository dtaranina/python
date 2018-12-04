# EASY-NORMAL

# Задача-1:
#
# Создать класс треугольник и реализовать в нем конструктор, методы для площади, периметра и вывод на экран.
# В конструкторе сделать проверку на возможность создания такого треугольника, если нет, то написать, что такой
# треугольник нельзя создать и сделать exit(1)

from math import radians, sin, cos


class Triangle:
    def __init__(self, side_a, side_b, angle):
        self.side_a = side_a
        self.side_b = side_b
        self.angle = angle
        self.__check = all([self.side_a, self.side_b, self.angle])

        if not self.__check or self.angle >= 180:
            print("Такой треугольник нельзя создать")
            exit(1)

    def get_square(self):
        return round(self.side_a * self.side_b / 2 * sin(radians(self.angle)), 2)

    def get_perimeter(self):
        return round(self.side_a ** 2 + self.side_b ** 2 - 2 * self.side_a * self.side_b * cos(radians(self.angle)), 2)

    def print_results(self):
        print(f"Площадь = {triangle.get_square()} мм², периметр = {triangle.get_perimeter()} мм")


a = int(input("Длина стороны а, мм = "))
b = int(input("Длина стороны b, мм = "))
ang = int(input("Угол между a и b = "))

triangle = Triangle(a, b, ang)

triangle.print_results()
