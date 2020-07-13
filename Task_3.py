# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

calendar_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring',
                 4: 'Spring', 5: 'Spring', 6: 'Summer',
                 7: 'Summer', 8: 'Summer', 9: 'Fall',
                 10: 'Fall', 11: 'Fall', 12: 'Winter'}
user_month_dict = int(input('Enter month №: '))
print(calendar_dict[user_month_dict])

calendar_list_month = ['Winter', 'Spring', 'Summer', 'Fall']
user_month_list = int(input('Enter month №: '))
if user_month_list == 12:
    print(calendar_list_month[0])
elif user_month_list > 8:
    print(calendar_list_month[3])
elif user_month_list > 5:
    print(calendar_list_month[2])
elif user_month_list > 2:
    print(calendar_list_month[1])
else:
    print(calendar_list_month[0])
