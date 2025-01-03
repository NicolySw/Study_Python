first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1.	В переменную first_result запишите список созданный при помощи сборки состоящий
# из длин строк списка first_strings, при условии, что длина строк не менее 5 символов.
first_result = [len(string) for string in first_strings if len(string) > 5]

# 2.	В переменную second_result запишите список созданный при помощи сборки
# состоящий из пар слов(кортежей) одинаковой длины. Каждое слово из
# списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

second_result = [(string_1, string_2) for string_1 in first_strings for string_2 in second_strings
                 if len(string_1) == len(string_2)]

# 3.	В переменную third_result запишите словарь созданный при помощи сборки,
# где парой ключ-значение будет строка-длина строки. Значения строк будут перебираться
# из объединённых вместе списков first_strings и second_strings. Условие записи пары в словарь - чётная длина строки.

third_result = {string: len_ for string in first_strings + second_strings
                if not (len_ := len(string)) % 2}

print(first_result)
print(second_result)
print(third_result)
