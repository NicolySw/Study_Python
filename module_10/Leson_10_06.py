import multiprocessing
import time
import threading


counter = 0


def fist_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
    print(f'Первый рабочий изменил значение счетчика {counter}')


def second_worker(n):
    global counter
    for i in range(n):
        counter += 1
        time.sleep(1)
    print(f'Второй рабочий изменил значение счетчика {counter}')


# tread1 = threading.Thread(target=fist_worker, args=(10, ))
# tread2 = threading.Thread(target=second_worker, args=(5, ))
# tread1.start()
# tread2.start()
if __name__ == '__main__':
    process1 = multiprocessing.Process(target=fist_worker, args=(10, ))
    process2 = multiprocessing.Process(target=second_worker, args=(15, ))
    process1.start()
    process2.start()
