# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = ['John', 10, 'Jack', 20, 'Sara', 30, 'Kate', 40]
print(my_list)
elem_count = 0
for i in range(len(my_list)):
    if i + elem_count < (len(my_list) - 1):
        tmp = my_list[i + elem_count]
        my_list[i + elem_count] = my_list[i + elem_count + 1]
        my_list[i + elem_count + 1] = tmp
        elem_count += 1
print(my_list)