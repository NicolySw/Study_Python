import logging


def add(a, b) -> object:
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Successful divided {a} and {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error("Na nol ne del", exc_info=True)
        return 0


def sqrt(a):
    if a >= 0:
        logging.info(f'Successful square root of {a}')
        return a ** 0.5
    else:
        logging.error("You cannot extract the root from a negative number", exc_info=True)
        return f'Действительных решений нет. \nМнимое решение: {(-a)**0.5}i'


def pow(a, b):
    return a ** b


if __name__ == '__main__':
    print(add(100, 3))
    # logging.debug('debug')
    # logging.info('info')
    # logging.warning('warning')
    # logging.error('error')
    # logging.critical('critical')
    logging.basicConfig(level=logging.INFO, filemode='w', filename="py.log",
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    print(div(3, 4))
    print(div(3, 0))
    print(sqrt(4))
    print(sqrt(-4))
