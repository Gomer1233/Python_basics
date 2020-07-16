# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self,speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_info(self):
        print(f'Car name is {self.name}\nCar color is {self.color}')

    def show_speed(self):
        print(self.speed)

    def go(self):
        print('Car is running')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turns {direction}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Yor speed is {self.speed}. Speed is exceeded, slow down!')
        else:
            print(self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Yor speed is {self.speed}. Speed is exceeded, slow down!')
        else:
            print(self.speed)

class SportCar(Car):
    def __init__(self, acceleration):
        self.acceleration = acceleration

class PoliceCar(Car):
    def __init__(self, type):
        self.type = type

town_car_1 = TownCar(100, 'Red', 'Kalina', False)
town_car_1.show_speed()
town_car_1.go()
town_car_1.stop()
town_car_1.turn('Left')
town_car_1.show_info()
