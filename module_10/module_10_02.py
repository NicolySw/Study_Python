"""
    Задача "За честь и отвагу!":
    Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
    1.	Атрибут name - имя рыцаря. (str)
    2.	Атрибут power - сила рыцаря. (int)
    А также метод run, в котором рыцарь будет сражаться с врагами:
    1.	При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
    2.	Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
    3.	В процессе сражения количество врагов уменьшается на power текущего рыцаря.
    4.	По прошествию 1 дня сражения (1 секунды) выводится строка "<Имя рыцаря> сражается <кол-во дней>...,
        осталось <кол-во воинов> воинов."
    5.	После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
    Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.
"""


import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_day = 1
        live = 100

        while live >= 1:
            live = live - self.power
            print(f'{self.name}, сражается {count_day} день(дня), осталось {live} воинов')
            count_day += 1
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {count_day-1} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')