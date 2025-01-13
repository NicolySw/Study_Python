import calk


def test_add():
    if calk.add(1, 2) == 3:
        print('Text add(a,b) is ok')
    else:
        print('Text add(a,b) is fail')


def test_sub():
    if calk.sub(1, 2) == -1:
        print('Text sub(a,b) is ok')
    else:
        print('Text sub(a,b) is fail')


def test_mul():
    if calk.mul(1, 2) == 2:
        print('Text mul(a,b) is ok')
    else:
        print('Text mul(a,b) is fail')

def test_div():
    if calk.div(2, 2) == 1:
        print('Text div(a,b) is ok')
    else:
        print('Text div(a,b) is fail')


test_add()
test_sub()
test_mul()
test_div()




