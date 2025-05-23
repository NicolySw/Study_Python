"""
    Задание "Программистам всё можно":
    Пора разрушать шаблоны привычного нам Python! Вот вас раздражает, что мы не можем сложить число(int)
    и строку(str)? Давайте исправим это недоразумение!
"""


def add_everything_up(a, b):
    try:
        sum_ = a + b
    except TypeError:
        sum_ = str(a) + str(b)
    return sum_


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

# Вывод в консоль:
# 123.456строка
# яблоко4215
# 130.456
