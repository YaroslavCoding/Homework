x = input('Какое задание хотите выполнить? ')

#1 задача
if x == '1':
    x = input('Введите строку: ')
    x = x.split(" ")
    x.reverse()
    print(x)
#2 задача
if x == '2':
    x = input('Введите строку: ')
    while len(x) < 15:
        x = input('Введите строку: ')
    print(x[0::2])
#3 задача
if x == '3':
    x = input('Введите список чисел через пробел: ')
    y = int(input('Введите степень: '))
    x = x.split(" ")
    for number in x:
        x[x.index(number)] = int(number)**y
    print(x)
#4 задача
if x == '4':
    x = input('Введите строку: ')
    y = input('Введите символ, содержащийся в строке: ')
    if y in x:
        x = x.replace(y, y + y)
        print(x)
    else:
        print('Данного символа нет в строке')
#5 задача
if x == '5':
    x = input('Введите строку: ')
    n1 = input('Какой символ посчитать: ')
    n2 = input('Какой символ посчитать: ')
    if n1 and n2 in x:
        z = x.count(n1)
        y = x.count(n2)
        print(f"{n1}: {z}, {n2}: {y}.")
#6 задача
if x == '6':
    x = input('Введите текст со скобками: ')
    start = x.find('(')
    end = x.find(')')
    if '(' not in x[end:] and ')' not in x[end:]:
        print(x[start + 1:end])
    else:
        print(x[start + 1:end])
        while '(' in x[end:] and ')' in x[end]:
            start = x.find('(', end + 1)
            end = x.find(')', end + 1)
            print(x[start + 1:end])








