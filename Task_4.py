# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_number = int(input('Input any integer: '))

my_list = []
while user_number > 0:
    temp_number = user_number % 10
    my_list.append(temp_number)
    user_number //= 10

print(max(my_list))






