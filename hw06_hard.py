#HARD

# Задание-1:
#
# Написать класс, который будет удобно использовать для работы с (на выбор что-нибудь одно)
# комплексными числами \ матрицами \ светофор \ микроволновка

# Чем логичнее код тем лучше

# Задание-2: не обязательно
#
# Написать консольную РПГ игру...
# Пример:

# <Характеристики персонажа>   <Характеристики врага>
# (HP, MP, Power, Defense)
#
# <Выбор действий>
# (Атаковать, Лечиться, .....)

from datetime import datetime, timedelta, time


class TrafficLight:

    def __init__(self, daytime, light, switch_green_to_red=40, switch_red_to_green=20, mode=1):
        self.daytime = daytime
        self.light = light
        self.switch_green_to_red = switch_green_to_red
        self.switch_red_to_green = switch_red_to_green
        self.mode = mode

    def switch_light(self):
        # if time(0, 0, 0) < self.daytime < time(5, 59, 59):
        #     return "yellow"
        # elif time(6, 0, 0) < self.daytime < time(10, 59, 59):
        #     return
        pass

    def get_the_mode(self):
        if time(0, 0, 0) < self.daytime < time(5, 59, 59):
            # return self.mode == "night mode on"
            return "night mode on"
        elif time(6, 0, 0) < self.daytime < time(10, 59, 59) or time(18, 0, 0) < self.daytime < time(19, 59, 59):
            # return self.mode == "rush hour mode on"
            return "rush hour mode on"
        elif time(11, 0, 0) < self.daytime < time(17, 59, 59) or time(20, 0, 0) < self.daytime < time(23, 59, 59):
            # return self.mode == "regular mode on"
            return "regular mode on"

    def night_mode_on(self):
        pass

    def rush_hour_mode_on(self):
        pass

    def turn_off_mode(self):
        pass




menu = {
    "On": None,
    "Off": None,
    "Night mode": None,
    "Rush hour mode": None,
    "Switch_time": None,
    "Show_light": None,
}

day_time = datetime.now().time()

traffic_light_1 = TrafficLight(day_time, "green")

print(traffic_light_1.get_the_mode())

print(traffic_light_1.daytime)

