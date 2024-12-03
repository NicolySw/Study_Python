def calc(line, count):
    try:
        operand_1, operation, operand_2 = line.split(' ')
    except ValueError:
        return f'в строке № {count} не хватает переменных'
    try:
        operand_1 = int(operand_1)
    except ValueError:
        return f'Ошибка перевода операнда {operand_1}'
    try:
        operand_2 = int(operand_2)
    except ValueError:
        return f'Ошибка перевода операнда {operand_2}'

    if operation == '+':
        return f'{operand_1} {operation} {operand_2} = {operand_1 + operand_2}'
    if operation == '-':
        return f'{operand_1} {operation} {operand_2} = {operand_1 - operand_2}'
    if operation == '*':
        return f'{operand_1} {operation} {operand_2} = {operand_1 * operand_2}'
    if operation == '//':
        return f'{operand_1} {operation} {operand_2} = {operand_1 // operand_2}'
    if operation == '/':
        return f'{operand_1} {operation} {operand_2} = {operand_1 / operand_2}'
    if operation == '%':
        return f'{operand_1} {operation} {operand_2} = {operand_1 % operand_2}'


count = 0
with open('calc.txt', 'r') as file:
    for line in file:
        count += 1
        print(calc(line, count))
