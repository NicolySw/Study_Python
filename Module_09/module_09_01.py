"""
    Задача "Вызов разом":
    Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
    1.	int_list - список из чисел (int, float)
    2.	*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
"""


def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except TypeError:
            print(f'Невозможно применить функцию {func.__name__} к списку {int_list}')
    return result


# Пример работы кода:
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

# Вывод на консоль:
# {'max': 20, 'min': 6} {'len': 4, 'sum': 50, 'sorted': [6, 9, 15, 20]}
