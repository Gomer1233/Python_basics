# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_f = open('Task_2.txt')

count_lines = 0
for i in my_f.readlines():
    count_lines += 1
    print(f'Total words in line {count_lines}: ', i.count(' ') + 1)
print(f'Total strings: {count_lines}')

my_f.close()



