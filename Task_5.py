# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

import functools

my_list = [i for i in range(100, 1001) if i % 2 == 0]

def reducer_func(el_prev, el):
    return el_prev * el

print(functools.reduce(reducer_func, my_list))