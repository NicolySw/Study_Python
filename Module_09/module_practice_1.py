animal = 'Мишка'
animals = ['Зайка', 'мишка', 'бегемотик']


def gen_repeat(n):
    def repeat(animal):
        return (animal[:2] + "-") * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animals[2]))


repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

result_2 = [func(animals[i]) for func in repetitions for i in range(len(animals))]
print(result_2)
