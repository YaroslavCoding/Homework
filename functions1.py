
x = input('Какую задачу хотите решить? ')

if x == '1': #1 задача

    def palindorme(x):
        x = x.lower()
        x = x.replace(" ", '')
        if x[0:] == x[::-1]:
            return True
        else:
            return False

    x = input('Введите строку: ')
    print(palindorme(x))

if x == '2':  # 2 задача

    def register(name, surname, patronymic, date_of_birth):
        return name + surname + patronymic + date_of_birth + 'г.р. зарегистрирован'

    name = input('Введите имя: ') + ' '
    surname = input('Введите фамилию: ') + ' '
    patronymic = input('Введите отчество: ') + ' '
    date_of_birth = input('Введите год рождения: ') + ' '

    print(register(name, surname, patronymic, date_of_birth))

if x == '3':  # 3 задача

    def find_max(a, b, c=0):
        x = []
        x.append(a)
        x.append(b)
        x.append(c)
        x = sorted(x, key=None, reverse=False)
        return x[-1]
    print(find_max()) # сюда надо передавать аргументы
