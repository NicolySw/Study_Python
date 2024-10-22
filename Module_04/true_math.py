"""
В true_math функция divide, которая принимает два параметра first и second.
Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать бесконечность.
Бесконечность можно импортировать из встроенной библиотеки math (from math import inf)
"""
import math


def divide(first, second):
    from math import inf
    if second != 0:
        return first/second
    else:
        return math.inf
