def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
print_params()

values_list = [1, 2, 3]
print_params(*values_list)

values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params(**values_dict)

values_list_2 = [1.2, 'Строка 55']
print_params(*values_list_2, 42)
