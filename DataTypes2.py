x = input('Какое задание хотите выполнить? ')

#1 задача
if x == '1':
    count = 0
    list_of_cities = []
    lis_of_checked_cities = []
    n = int(input('Введите количество городов: '))
    for cities in range(n): #здесь заносим города в список
        x = input('Введите город: ')
        list_of_cities.append(x)
    for city in list_of_cities: #здесь проверяем города из списка, добавляя каждый проверенный в отдельный список, чтобы не происходила проверка одного и того же значения
        if city not in lis_of_checked_cities:
            if list_of_cities.count(city) > 1:
                count += list_of_cities.count(city)
                lis_of_checked_cities.append(city)
    print(count)
#2 задача
if x == '2':
    x = input('Введите строку: ')
    x = x.strip()
    x = list(x)
    x[0] = x[0].upper()
    x = ''.join(x)

    if '.' in x:
        start = -1
        count = x.count('.')
        try:
            for i in range(count):
                start = x.find('.', start+1)
                str1 = x[:start + 1]
                str2 = x[start + 1:].strip()
                letter = str2[0].upper()
                str2 = str2[1:]    #отделяем вторую часть строки от буквы, которую надо озаглавить
                x = str1 + ' ' + letter + str2
        except IndexError:
            pass
    if '!' in x:
        start = -1
        count = x.count('!')
        try:
            for i in range(count):
                start = x.find('!', start+1)
                str1 = x[:start + 1]
                str2 = x[start + 1:].strip()
                letter = str2[0].upper()
                str2 = str2[1:]    #отделяем вторую часть строки от буквы, которую надо озаглавить
                x = str1 + ' ' + letter + str2
        except IndexError:
            pass
    if '?' in x:
        start = -1
        count = x.count('?')
        try:
            for i in range(count):
                start = x.find('?', start+1)
                str1 = x[:start + 1]
                str2 = x[start + 1:].strip()
                letter = str2[0].upper()
                str2 = str2[1:]    #отделяем вторую часть строки от буквы, которую надо озаглавить
                x = str1 + ' ' + letter + str2
        except IndexError:
            pass
    print(x)

#3 задача
if x == '3':
    x = input('Введите первую строку: ')
    y = input('Введите вторую строку: ')
    check1 = set(x).issuperset(set(y)) #проверяем, является ли одна переменная подмножеством другой и наоборот
    check2 = set(y).issuperset(set(x))
    if check1 == True and check2 == True and len(x) == len(y):
        print('Строки являются анаграммами')
    else:
        print('Строки не являются анаграммами')
#4 задача
if x == '4':
    x = set(sorted(input('Введите фамилии решивших задачи по алгебре: ').split(' ')))
    y = set(sorted(input('Введите фамилии решивших задачи по геометрии: ').split(' ')))
    z = set(sorted(input('Введите фамилии решивших задачи по тригонометрии: ').split(' ')))
    winner = x & y & z #находим общий элемент множества
    if not winner:
        print('Никто не решил все три!')
    else:
        winner = ' '.join(winner)
        print('Все три удалось решить: ' + winner)












