"""
    Задача "Потоковая запись в файлы":

    Необходимо создать функцию wite_words(word_count, file_name), где word_count -
    количество записываемых слов, file_name - название файла, куда будут записываться слова.
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
    с прерыванием после записи каждого на 0.1 секунду.

    Сделать паузу можно при помощи функции sleep из модуля time, предварительно импортировав её: from time import sleep.
    В конце работы функции вывести строку "Завершилась запись в файл <название файла>".

"""
import time
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    file = open(file_name, 'a')
    for i in range(word_count):
        time.sleep(0.1)
        file.write(f'Какое-то слово № {str(i)} \n')
    file.close()
    print(f'Завершилась запись в файл {file_name}')


start_time = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
print(f'Продолжительность последовательной работы {datetime.now() - start_time}')

start_time = datetime.now()
thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
print('Продолжительность работы потоков', datetime.now() - start_time)
