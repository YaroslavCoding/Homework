def create_list(x):  #функция создания списка
    x = x.split(' ')
    for element in range(len(x)):
        x[element] = int(x[element])
    return x

def max_number(x):  #рекурсивная функция
    if len(x) == 1:
        return x
    elif x[len(x) - 1] >= x[len(x) - 2]:
        del x[len(x) - 2]
    elif x[len(x) - 1] <= x[len(x) - 2]:
        del x[len(x) - 1]
    return max_number(x)

x = input('Введите числа через пробел: ')
x = create_list(x)
print(max_number(x))
