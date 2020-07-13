# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('Task_5.txt', 'w') as my_f:
    my_f.write('3 4 5 6 7 8')

with open('Task_5.txt') as my_f:
    count = 0
    for i in my_f:
        g = i.split()
        for i in g:
            i = int(i)
            count += i
    print(count)



