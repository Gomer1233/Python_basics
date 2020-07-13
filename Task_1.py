# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

age = 18
height = 180
weight = 80
name = 'John'

print(age, height, weight)

age = int(input('Enter age: '))
height = int(input('Enter height: '))
weight = int(input('Enter weight: '))
name = input('Enter name: ')

print(f'name: {name} age: {age} height: {height} weight: {weight}')