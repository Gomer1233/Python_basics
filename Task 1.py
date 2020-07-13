# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(num_1, num_2):
    try:
        num_1 / num_2
    except ZeroDivisionError:
        return 'Zero division is forbidden! Second number must be > 0'
    return round((num_1 / num_2), 2)

num_1 = float(input('Enter first number: '))
num_2 = float(input('Enter second number: '))

print(div(num_1, num_2))
