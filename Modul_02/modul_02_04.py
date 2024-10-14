numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []     # список простых чисел
not_primes = []  # список не простых чисел
for i in range(0, len(numbers), 1):
    if numbers[i] > 3:
        for j in range(2, numbers[i]-1):
            k = numbers[i]
            flag = False
            if numbers[i] % j != 0:
                flag = True
            else:
                break
        if flag:
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])

    else:
        if numbers[i] != 1:
            primes.append(numbers[i])
print("Простые числа из списка:", primes)
print("Составные числа и списка: ", not_primes)
