"""
    Домашнее задание по уроку "Пространство имен"
"""


# Создайте новую функцию test_function
# Создайте внутри test_function другую функцию - inner_function,
# Эта функция должна печатать значение "Я в области видимости функции test_function"

# Вызовите функцию inner_function внутри функции test_function
# Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function()  вызов этой функции вне функции в которой она описана приводит к ошибке:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?


