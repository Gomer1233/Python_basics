# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

my_str = input('Enter any number of words divided by space: ')

my_list = my_str.split()

for i, r in enumerate(my_list):
    print(i + 1, r[0:11])
