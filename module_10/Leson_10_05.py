from threading import Thread, Event
import time


def fist_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять задачу')
    time.sleep(5)
    print("Первый рабочий закончил выполнять задачу")


def second_worker():
    print("Второй рабочий приступил к своей задаче")
    time.sleep(18)
    print("Второй рабочий закончил выполнять задачу")
    event.set()


event = Event()
thread1 = Thread(target=fist_worker)
thread2 = Thread(target=second_worker)

thread1.start()
thread2.start()



# event.wait(timeout=5)

