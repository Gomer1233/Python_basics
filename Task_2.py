# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_user = int(input('Enter time in seconds: '))
time_hour = time_user // 60 // 60
time_min = time_user // 60 % 60
time_sec = time_user % 60

print(f'{time_hour}:{time_min}:{time_sec}')
