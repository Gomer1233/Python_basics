# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

g_1 = (1, {'Name': input('Enter good 1 name: '), 'Price': input('Enter goods 1 price: '),
           'Quantity': input('Enter goods 1 quantity'), 'Unit': input('Enter metrics: ')})
g_2 = (2, {'Name': input('Enter good 2 name: '), 'Price': input('Enter goods 2 price: '),
           'Quantity': input('Enter goods 2 quantity'), 'Unit': input('Enter metrics: ')})
g_3 = (3, {'Name': input('Enter good 3 name: '), 'Price': input('Enter goods 3 price: '),
           'Quantity': input('Enter goods 3 quantity'), 'Unit': input('Enter metrics: ')})

name_list = [g_1[1].get('Name')]
price_list = [g_1[1].get('Price')]
qty_list = [g_1[1].get('Quantity')]
unit_list = [g_1[1].get('Unit')]

name_list.append(g_2[1].get('Name'))
price_list.append(g_2[1].get('Price'))
qty_list.append(g_2[1].get('Quantity'))
unit_list.append(g_2[1].get('Unit'))

name_list.append(g_3[1].get('Name'))
price_list.append(g_3[1].get('Price'))
qty_list.append(g_3[1].get('Quantity'))
unit_list.append(g_3[1].get('Unit'))

new_dict = {'Name': name_list,
            'Price': price_list,
            'Quantity': qty_list,
            'Unit': set(unit_list)}

print(new_dict)
