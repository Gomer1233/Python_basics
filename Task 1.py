# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys

def salary(prod, rate, bonus):
    return int(prod) * int(rate) + int(bonus)


_, prod, rate, bonus = sys.argv

print(salary(prod, rate, bonus))