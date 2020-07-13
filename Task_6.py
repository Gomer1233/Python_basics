# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

day_one_result = int(input('Enter the distance that you are currently able to run: '))
goal = int(input('Enter the distance that you wish to cover: '))
day_counter = 1

while day_one_result < goal:
    day_counter += 1
    day_one_result += day_one_result * 0.1
print(f'You will need {day_counter} days to achive your goal. Time to train!')
