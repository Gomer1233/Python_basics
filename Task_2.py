# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

class Coat(Cloth):
    @abstractmethod
    def __init__(self, size):
        self.size = size

class Suit(Cloth):
    @abstractmethod
    def __init__(self, height):
        self.height = height

class Coat(Cloth):
    def __init__(self):
        self.size = 46

    @property
    def cloth_cons_coat(self):
        cons = self.size / 6.5 + 0.5
        return round(cons, 2)

class Suit(Cloth):
    def __init__(self):
        self.height = 8

    @property
    def cloth_cons_suit(self):
        cons = self.height * 2 + 0.3
        return round(cons, 2)


coat = Coat()
suit = Suit()
print(coat.cloth_cons_coat)
print(suit.cloth_cons_suit)
print(round(coat.cloth_cons_coat + suit.cloth_cons_suit, 2))