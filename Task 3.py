# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    arg_list = [arg_1, arg_2, arg_3]
    arg_list.sort()
    max_list = [arg_list.pop(), arg_list.pop()]
    return sum(max_list)


print(my_func(9000, 20, 1000))
