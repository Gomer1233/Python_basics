# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('Task_4.txt') as my_f:
    dict = {}
    for i in my_f:
        a, b, c = i.split()
        if c == '1':
            c = 'Odin'
            my_new_f = open('Task_4_1.txt', 'w')
            my_new_f.writelines(a + ' ' + '-' + ' ' + c + '\n')
        if c == '2':
            c = 'Dva'
            my_new_f = open('Task_4_1.txt', 'a')
            my_new_f.writelines(a + ' ' + '-' + ' ' + c + '\n')
        if c == '3':
            c = 'Tri'
            my_new_f = open('Task_4_1.txt', 'a')
            my_new_f.writelines(a + ' ' + '-' + ' ' + c + '\n')
        if c == '4':
            c = 'Chetire'
            my_new_f = open('Task_4_1.txt', 'a')
            my_new_f.writelines(a + ' ' + '-' + ' ' + c + '\n')
