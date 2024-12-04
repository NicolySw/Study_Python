def count_calls():
    """
        Функция, подсчитывающая вызовы остальных функций.
    """
    global calls
    calls += 1


def string_info(string):
    """
       Функция принимает аргумент - строку и возвращает кортеж из:
       длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    """
    count_calls()
    return [len(string), string.upper(), string.lower()]


def is_contains(string, list_):
    """
       Принимает два аргумента: строку и список, и возвращает True, если строка
       находится в этом списке, False - если отсутствует.
    """
    count_calls()
    list_1 = []
    for i in range(len(list_)):
        list_1.append((list_[i].lower()))
    if string.lower() in list_1:
        return True
    else:
        return False


calls = 0
print(string_info("Capybara"))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
