x = input('какую задачу хотите решить?')

#задача 1
if x == '1':
    sum = 0
    x = input('Введите число:')
    for i in x:
        i = int(i)
        sum += i
    print(f'сумма цифр в числе - {sum}')

#задача 2
elif x == '2':
    x = int(input('введите число для факториала:'))
    n = 1 #факториал
    for i in range(1, x + 1):
        n = n * i
    print(f'факториал {x} - {n}')

#задача 3
elif x == '3':
    x = int(input('введите число n:'))
    for i in range(x+1):
        if i % 7 == 0 and i != 0:
            print(i)


