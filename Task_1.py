# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('test.txt', 'w')

while True:
    user_data = input('Enter new line. To finish leave empty: ')
    if user_data == '':
        break
    else:
        my_f.write(user_data + '\n')

my_f.close()