import inspect

import requests

some_string = 'I am a string'
some_number = 42
some_list = [some_string, some_number]


def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)


class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)


some_object = SomeClass()
func = some_function
#
# print(some_function.__name__)
# print(SomeClass.__name__)
# print(requests.__name__)
# print(func.__name__)
#
#
# print(type(some_number) is int)
# print(type(some_number) is str)


# # pprint(dir(some_number))
# pprint(dir(some_list))

# Пример 1 - функция hasattr() -проверяет на существование атрибута
'''
attr_name = 'attribute_2'
print(hasattr(some_object, attr_name))
print(hasattr(some_object, 'attribute_1'))
'''
"""
# Пример 2 - функция getattr - получение атрибута

print(getattr(some_object, "attribute_1"))
print(getattr(some_object, "attribute_2", "Этого не может быть"))

for attr_name in dir(some_object):
    attr = getattr(requests, attr_name)
    print(attr_name, type(attr))
"""
'''
# Пример 3 - функция callable() - проверка на то, можем ли мы вызвать этот объект
print(callable(some_string))
print(callable(some_function))
print(callable(some_object.attribute_1))
print(callable(some_object.some_class_method))

# Пример 4 - функция isinstance - мы можем определить, является ли определенны объект экземпляром указанного класса.

print(isinstance(some_number, str))
print(isinstance(some_number, int))
print(isinstance(some_number, SomeClass))
print(isinstance(some_object, SomeClass))

'''
# Пример 5 inspect
# Модуль собирает самые методы и классы для отображения интроспективной информации

print(inspect.ismodule(requests))
print(inspect.isclass(some_object))
print(inspect.isfunction(requests))
print(inspect.isbuiltin(requests))

some_function_module = inspect.getmodule(some_function)
print(type(some_function_module), some_function_module)
