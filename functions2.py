from functools import reduce

def create_list(x): #участок кода с созданием спиская повторяется во всех задачах, поэтому создана функция
    x = x.split(' ')
    for element in range(len(x)):
        x[element] = int(x[element])
    return x

x = input('Какую задачу решить? ')

if x == '1':
    while True:
        x = input('Введите через пробел последовательность чисел: ') #здесь создается вводимый пользователем числовой список
        x = create_list(x)
        y = input('Введите через пробел последовательность чисел: ') #здесь создается вводимый пользователем числовой список
        y = create_list(y)

    lamba_function = lambda x, y: x + y
    sum = map(lamba_function, x, y)

     if len(x) > len(y):
        sum = list(sum)
        sum.extend(x[len(y):])
        print(sum)
    elif len(y) > len(x):
        sum = list(sum)
        sum.extend(y[len(x):])
        print(sum)
    else:
        print(list(sum))

if x == '2':
    x = input('Введите через пробел последовательность чисел: ')  # здесь создается вводимый пользователем числовой список
    x = create_list(x)

    lamba_function = lambda x: x % 19 == 0 or x % 13 == 0
    filtered = filter(lamba_function, x)
    print(list(filtered))

if x == '3':
    x = input('Введите через пробел последовательность чисел: ')  # здесь создается вводимый пользователем числовой список
    x = create_list(x)

    lamba_function = lambda x, y: x if x > y else y
    reduced = reduce(lamba_function, x)
    print(reduced)

