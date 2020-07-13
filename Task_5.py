# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input('Enter you companys revenue: '))
cost = int(input('Enter you companys costs: '))
profit = revenue - cost

if revenue > cost:
    print('Your company is profitable, congrats!')
    profit = revenue - cost
    profitability = profit / revenue
    print('Your profitability is:', round(profitability, 2))
elif revenue < cost:
    print('Your company is unprofitable, too bad!')
else:
    print('Its even. You have to push harder!')

staff = int(input('Enter the number of employees: '))
profit_per_staff = profit / staff

print('Profit per emoloyee is:', round(profit_per_staff, 2))