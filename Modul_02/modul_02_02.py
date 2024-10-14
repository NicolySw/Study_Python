first = input("Введите число: ")
second = input("Введите число: ")
third = input("Введите число: ")

if first == second and first == third:
    print('3')
elif first == second or second == third or third == first:
    print('2')
else:
    print('0')
