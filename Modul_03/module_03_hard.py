def sum_(data_):
    global summa
    if isinstance(data_, dict):                       # Если словарь - передаем рекурсивно на функцию ключи и значения
        for key, value in data_.items():
            sum_(key)
            sum_(value)
    if isinstance(data_, (list, tuple, set)):         # Если список, кортеж или множество передаем обратно на функцию
        for item in data_:                            # значения item
            sum_(item)

    if isinstance(data_, str):                        # Если строк - считаем ее длину
        summa += len(data_)
    if isinstance(data_, (int, float)):                        # Если число - просто прибавляем его к сумме
        summa += data_
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = 0
for i in range(len(data_structure)):
    sum_(data_structure[i])
print(f'Сумма всех элементов: {summa}')
