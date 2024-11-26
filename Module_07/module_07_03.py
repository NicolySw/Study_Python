"""
    Цель: применить на практике оператор with, вспомнить написание кода в парадигме ООП.
    Задача "Найдёт везде":
    Напишите класс WordsFinder, объекты которого создаются следующим образом:
    WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
    Объект этого класса должен принимать при создании неограниченного количество названий файлов и записывать их в атрибут file_names в виде списка или кортежа.

    Также объект класса WordsFinder должен обладать следующими методами:
    get_all_words - подготовительный метод, который возвращает словарь следующего вида:
    {'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
    Где:
    1.	'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
    2.	['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.
    Алгоритм получения словаря такого вида в методе get_all_words:
    1.	Создайте пустой словарь all_words.
    2.	Переберите названия файлов и открывайте каждый из них, используя оператор with.
    3.	Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
    4.	Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке. (тире обособлено пробелами, это не дефис в слове).
    5.	Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
    6.	В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

    find(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
    count(self, word) - метод, где word - искомое слово. Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
    В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
    Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().
"""


class WordsFinder:
    def __init__(self, file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_words = {}
        stripped_line = ''
        a = 0
        with open(self.file_name, encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    char = [",", ".", "=", "!", "?", ";", ":", " - ", " "]
                    for i in range(0, len(char)):
                        word = word.replace(char[i], "")
                    stripped_line += word.lower() + ' '
            all_words[self.file_name] = stripped_line.split()
        return all_words

    def find(self, word):
        dict_ = {}
        for name, word_ in self.get_all_words().items():
            count = 0
            for char in word_:
                count += 1
                if char == word.lower():
                    dict_[name] = count
                    break
        return dict_

    def count(self, word):
        dict_ = {}
        for name, word_ in self.get_all_words().items():
            count = 0
            for char in word_:
                if char == word.lower():
                    count += 1
                    dict_[name] = count
        return dict_



# for name, words in get_all_words().items():
# Логика методов find или count


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


#
# Вывод на консоль:
# {'test_file.txt': ["it's", 'a', 'text', 'for', 'task', 'найти', 'везде', 'используйте', 'его', 'для', 'самопроверки',
#                    'успехов', 'в', 'решении', 'задачи', 'text', 'text', 'text']}
# {'test_file.txt': 3}
# {'test_file.txt': 4}
#
# Запустите этот код с другими примерами предложенными здесь.
# Если решение верное, то результаты должны совпадать с предложенными.
#
# Примечания:
# 1.	Регистром слов при поиске можно пренебречь. ('teXT' ~ 'text')
# 2.	Решайте задачу последовательно - написав один метод, проверьте результаты его работы.

#
# example_str = "T i m! e, w ?e ?b!"
# char = [",", ".", "=", "!", "?", ";", ":", " - ", " "]
# for i in range(0, len(char)):
#     example_str = example_str.replace(char[i], "")
#
# print(example_str)
