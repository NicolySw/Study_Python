import matplotlib.pyplot as plt
import numpy as np

# линейный график
plt.plot([1, 2, 3, 4])
plt.ylabel('Линейный график')
plt.show()

# пример столбчатой диаграммы
x = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май']
y = [2, 4, 3, 1, 7]
plt.bar(x, y, label='Величина прибыли') #Параметр label позволяет задать название величины для легенды
plt.xlabel('Месяц года')
plt.ylabel('Прибыль, в млн руб.')
plt.title('Пример столбчатой диаграммы')
plt.legend()
plt.show()

# круговая диаграмма
vals = [24, 17, 53, 21, 35]
labels = ["Ford", "Toyota", "BMW", "Audi", "Jaguar"]

plt.pie(vals, labels=labels)
plt.title("Распределение марок автомобилей на дороге")
plt.show()

# Построение квадратичной функции с помощью numpy

x = np.linspace(-2, 2, 100)        # используется для генерации последовательности чисел
                                            # в линейном пространстве с одинаковым размером шага

y = x ** 2
fig = plt.figure(figsize=(10, 5))
plt.plot(x, y)

plt.show()
