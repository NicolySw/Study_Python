# Задание:
# Напишите 2 функции:
# 1.	Функция, которая складывает 3 числа (sum_three)
# 2.	Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.
# Пример:

def is_prime(func):
    def wrapper(*args, **kwargs):
        flag = False
        numbers = func(*args, **kwargs)
        if numbers > 3:
            for j in range(2, numbers - 1):
                if numbers % j != 0:
                    flag = True
                else:
                    flag = False
                    break
        if flag:
            return "Простое"
        else:
            return "Составное"

    return wrapper


@is_prime
def sum_three(*numbers):
    print(sum(numbers))
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)
