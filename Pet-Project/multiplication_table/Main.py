from functools import partial
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import time
import numexpr as ne
import threading

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")


def change(n, button_identities, dict_question, correct_answer, window1):

    bname = (button_identities[n-1])
    print(n)

    if dict_question[n] == correct_answer:
        bname.configure(text="Верно")

        # window1.destroy()
        # test(n)
    else:
        bname.configure(text="Неверно")
        bname.destroy()


def next_(n, window1):
    window1.destroy()
    test(n)

def test(n):
    window1 = Tk()
    window1.title(f'Изучаем умножение на {n}')
    window1.geometry(f"{window_width}x{window_height}+{screen_wight // 2 - window_width // 2}+"
                     f"{screen_height // 2 - window_height // 2}")  # устанавливаем размеры окна
    window1.resizable(False, False)

    if n == 10:
        example = f'{randint(1,10)}*{randint(1,10)}'
    else:
        example = f'{n}*{randint(1,10)}'

    label_1 = Label(window1, text=example, font=("Arial", 20))
    label_1.grid(column=0, row=0, columnspan=4)

    for c in range(4): window1.columnconfigure(index=c, weight=1)
    for r in range(5): window1.rowconfigure(index=r, weight=1)

    dict_question = {}
    correct_answer = f"{ne.evaluate(example)}"

    for i in range(1, 5):
        dict_question[i] = str(randint(1,100))
    rand = randint(1, 4)
    dict_question[rand] = correct_answer

    ii = 0
    button_identities = []
    for r in range(1, 2, 1):
        for c in range(4):
            ii += 1
            btn_1 = ttk.Button(window1, text=dict_question.get(ii), command=partial(change, ii, button_identities,
                                                                                    dict_question, correct_answer,
                                                                                    window1))
            btn_1.grid(row=r, column=c)
            button_identities.append(btn_1)

    btn_2 = ttk.Button(window1, text="Следующий", command=partial(next_,n, window1))
    btn_2.grid(row=2, column=0, columnspan=4)

    btn_3 = ttk.Button(window1, text="Закрыть", command=window1.destroy)
    btn_3.grid(row=3, column=0, columnspan=4)



button_identities = []
root = Tk()  # создаем корневой объект - окно
root.title("Изучаем умножение")  # устанавливаем заголовок окна
screen_wight = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 600

root.geometry(f"{window_width}x{window_height}+{screen_wight // 2 - window_width // 2}+"
              f"{screen_height // 2 - window_height // 2}")  # устанавливаем размеры окна
root.resizable(False, False)
# icon = PhotoImage(file="img_1.png")
# root.iconphoto(True, icon)

label = Label(text="Выбрать множитель", font=("Arial", 14))  # создаем текстовую метку
#label.pack()  # размещаем метку в окне

i = 0
label.grid(column=0, row=0, columnspan=3)
for c in range(4): root.columnconfigure(index=c, weight=1)
for r in range(5): root.rowconfigure(index=r, weight=1)

for r in range(1, 4, 1):
    for c in range(3):
        i += 1
        btn = ttk.Button(text=f"{i}", command=partial(test, i))
        btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=1, pady=1)

btn = ttk.Button(text="1-10", command=partial(test, 10))
btn.grid(row=4, column=0, ipadx=6, ipady=6, padx=1, pady=1, columnspan=3)



root.protocol("WM_DELETE_WINDOW", finish)
root.mainloop()

