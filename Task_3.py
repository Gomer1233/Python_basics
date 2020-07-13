# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_dict = {}
with open("Task_3.txt") as file:
    for line in file:
        key, value = line.split()
        my_dict[key] = value
    print(my_dict)

    # print(f'List of employee with salary less then 20000:\n')
    # salary = []
    # for i, k in my_dict.items():
    #     salary.append(k)
    #     if k < 20000:
    #         print(i)
    # print(f'Average salary is: {round((sum(salary) / len(salary)), 2)}')
    #
    #
