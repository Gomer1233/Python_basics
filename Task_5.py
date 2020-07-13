# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_num(str_num):
    total = 0
    list_num = str_num.split()
    while 'q' in list_num:
        for i in list_num:
            if i == 'q':
                list_num.remove(i)
    for i in range(len(list_num)):
        list_num[i] = int(list_num[i])
    total += sum(list_num)
    return total

total = 0

while True:
    user_numbers = input('Enter integers divided by space. If you want to quit enter Q: ').lower()
    total += (sum_num(user_numbers))
    print(f'Total sum is: {total}', end='\n')
    if 'q' in user_numbers:
        break

# Second solution
# def sum_num():
#     total = 0
#     while True:
#         user_numbers = input('Enter integers divided by space. If you want to quit enter Q: ').lower()
#         total += sum(list(map(lambda n_1: int(n_1), filter(str.isdigit, user_numbers))))
#         print(f'Total sum is: {total}')
#         if 'q' in user_numbers:
#             break
#     return total
#
# print(sum_num())