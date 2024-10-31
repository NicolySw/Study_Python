import tkinter as tk
import books as bs


def add(book):
    pass


def search():
    global str_
    str_ = text_entry.get()
    flag_ = False
    for key, value in bs.books_.items():
        if str_ == key:
            flag_ = True
            if value[1]:
                print("В базе найдена книга: ", key, value[0])

                window1 = tk.Tk()
                window1.title('Библиотека 1.0')
                window1.geometry('400x250')
                window1.resizable(False, False)
                lab_1 = tk.Label(window1, text=f'В базе найдена книга: {key} {value[0]}')
                lab_1.place(x=50, y=30)
                lab_1 = tk.Label(window1, text="Хотите ее взять?")
                lab_1.place(x=50, y=55)

                but_ = tk.Button(window1, text="Взять", width=10, command=take_book)
                but_.place(x=50, y=200)
                but_close = tk.Button(window1, text="Отменить", width=10, command=window1.destroy)
                but_close.place(x=150, y=200)

                window1.mainloop()

            else:
                window2 = tk.Tk()
                window2.title('Библиотека 1.0')
                window2.geometry('400x250')
                window2.resizable(False, False)
                lab_2 = tk.Label(window2, text=f'В базе найдена книга: {key} {value[0]}, но она уже взята')
                lab_2.place(x=50, y=30)
                but2_close = tk.Button(window2, text="Отменить", width=10, command=window2.destroy)
                but2_close.place(x=150, y=200)
                window2.mainloop()
    if not flag_:
        window_not_found = tk.Tk()
        window_not_found.title('Библиотека 1.0')
        window_not_found.geometry('200x200')
        window_not_found.resizable(False, False)
        lab_not_found = tk.Label(window_not_found, text=f'В базе книга не найдена')
        lab_not_found.place(x=10, y=30)
        but_not_found = tk.Button(window_not_found, text="Отменить", width=10, command=window_not_found.destroy)
        but_not_found.place(x=50, y=100)
        window_not_found.mainloop()
        print("Книга не найдена")


def take_book():
    global str_
    str_ = text_entry.get()
    window_take = tk.Tk()
    window_take.title('Библиотека 1.0')
    window_take.geometry('300x200')
    window_take.resizable(False, False)
    lab_take = tk.Label(window_take, text=f'Книга взята')
    lab_take.place(x=10, y=30)
    but_take = tk.Button(window_take, text="Отменить", width=10, command=window_take.destroy)
    but_take.place(x=50, y=100)
    for key, value in bs.books_.items():
        if str_ == key:
            value[1] = False
    window_take.mainloop()


def put_book():
    pass


str_ = ''
window = tk.Tk()
window.title('Библиотека 1.0')
window.geometry('350x350')
window.resizable(False, False)
lab_ = tk.Label(window, text="Введите имя автора")
lab_.place(x=50, y=30)
text_entry = tk.Entry(window)
text_entry.place(x=50, y=50, width=200)

button_search = tk.Button(window, text="Найти", width=10, command=search)
button_search.place(x=50, y=300)

button_cancel = tk.Button(window, text="Отменить", width=10, command=window.destroy)
button_cancel.place(x=150, y=300)

window.mainloop()
