# - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
# - Выполните операции вывода кортежа immutable_var на экран.
immutable_var = (2, 1, 'dd')
print(immutable_var)
immutable_var[2] = 0
# Изменение значений переменных:
# - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# Изменить кортеж нельзя, если в него не входят списки, другими словами можно поменять только списки в составе кортежа.

# - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
# - Измените элементы списка mutable_list.
# - Выведите на экран измененный список mutable_list.

mutable_list = [1, 2, 3]
print(mutable_list)
mutable_list[2] = 'ee'
print(mutable_list)
