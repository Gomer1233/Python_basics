# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

with open('Task_7.txt') as my_file:
    list = []
    dict = {}
    total_profit = 0
    count_prof = 0
    for i in my_file:
        str = i.split()
        profit = int(str[2]) - int(str[3])
        dict[str[0]] = profit
    for i, k in dict.items():
        if k > 0:
            total_profit += k
            count_prof += 1
    aver_profit = {'average_profit': total_profit / count_prof}
    list.append(dict)
    list.append(aver_profit)
    print(list)

with open('Task_7.json', 'w') as my_json:
    json.dump(list, my_json)

