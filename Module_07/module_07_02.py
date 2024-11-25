"""
    Задача "Записать и запомнить":
    Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла
    для записи, strings - список строк для записи.

    Функция должна:
    1.	Записывать в файл file_name все строки из списка strings, каждая на новой строке.
    2.	Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
        а значением - записываемая строка. Для получения номера байта начала строки используйте
        метод tell() перед записью.

    Пример полученного словаря:
    {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
    Где:
    1, 2 - номера записанных строк.
    0, 16 - номера байт, на которых началась запись строк.
    'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
"""


def custom_write(file_name, strings):
    number_string = 0
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        number_string += 1
        strings_positions[str(number_string), str(file.tell())] = string
        file.write(string+'\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


#
# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

