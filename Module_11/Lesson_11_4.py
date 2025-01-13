import sys
from pprint import pprint

"""
pprint(dir(sys))
# путь к интерпретатору Python
pprint(sys.executable)

# в какой операционной системе работаем
pprint(sys.platform)

# Текущая версия Python
pprint(sys.version)
pprint(sys.version_info)

# список, содержащий параметры командной строки, если она была задана
pprint(sys.orig_argv)

# путь поиска модуля, список каталогов, в которых Python будет искать модули во время импорта
pprint(sys.path)

# словарь, отображающий имена модулей и объекты модулей для всех загруженных в текущий момент модулей
pprint(sys.modules)

# Псевдо-модуль, содержащий встроенный интерпретатор объекты  
pprint(__builtins__)
pprint(dir(__builtins__))

"""
'''
# Пример запуска кода при версии 3.12.3
print(sys.version.split())


def func(x):
    if sys.version.split(' ')[0] == "3.12.3":
        return x + 10
    else:
        raise Exception('Недопустимая версия')


print(func(3))
'''


def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


sys.setrecursionlimit(5000)
sys.set_int_max_str_digits(10000)
print(factorial(2000))
