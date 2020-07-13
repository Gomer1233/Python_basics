# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def profile(name, surname, year_of_birth, city, email, phone):
    return name, surname, year_of_birth, city, email, phone


print(profile(name='Andy', surname='Dick',
              year_of_birth=1990, city='London',
              email='andy@mail.ru', phone='926 - 76 - 55'))
