x = input('Какую задачу хотите решить? ')
#P.S. на первую задачу ушло 58 строк, так как я не слишком силен в написании компактного кода для математических задач)

if x == '1': #1 задача
    result = 1
    divisor = 2
    prime_numbers_x = []
    prime_numbers_y = []
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    if x / y == 1:
        print(f'НОК - {x}')
    elif x % y == 0 or y % x == 0:
        print(f'НОК - {max(x,y)}')
    else:
        while True:
            if x % divisor == 0:
                x = x / divisor
                prime_numbers_x.append(divisor)
                if x == 1:
                    divisor = 2
                    break
            else:
                divisor += 1
        while True:
            if y % divisor == 0:
                y = y / divisor
                prime_numbers_y.append(divisor)
                if y == 1:
                    divisor = 2
                    break
            else:
                divisor += 1
        if len(prime_numbers_x) > len(prime_numbers_y):
            for i in prime_numbers_y:
                if i not in prime_numbers_x:
                    prime_numbers_x.append(i)
            for i in prime_numbers_x:
                result *= i
            print(f'НОК - {result}')
        elif len(prime_numbers_y) > len(prime_numbers_x):
            for i in prime_numbers_x:
                if i not in prime_numbers_y:
                    prime_numbers_y.append(i)
            for i in prime_numbers_y:
                result *= i
            print(f'НОК - {result}')
        elif len(prime_numbers_x) == len(prime_numbers_y) and sum(prime_numbers_x) > sum(prime_numbers_y):
            for i in prime_numbers_x:
                if i not in prime_numbers_y:
                    prime_numbers_y.append(i)
            for i in prime_numbers_y:
                result *= i
            print(f'НОК - {result}')
        elif len(prime_numbers_x) == len(prime_numbers_y) and sum(prime_numbers_x) < sum(prime_numbers_y):
            for i in prime_numbers_y:
                if i not in prime_numbers_x:
                    prime_numbers_x.append(i)
            for i in prime_numbers_x:
                result *= i
            print(f'НОК - {result}')

if x == '2': #2 задача
    x = []   #список с простыми числами

    def isprime(number):   #функция проверки числа на простоту
        for i in range(2, int(n ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    n = int(input('Введите n-число: '))
    for number in range(1, n + 1):
        if isprime(number):
            x.append(number)
    print(f'Список простых чисел до n - {x}')

if x == '3': #3 задача
    x = [] #  список делителей числа n
    n = int(input('Введите n-число: '))

    def divisor(n, number): #функция проверки на делитель (делится ли нацело)
        if n % number == 0:
            return True
        else:
            return False

    for number in range(1,n + 1):
        if divisor(n, number):
            x.append(number)

    print(f'Список делителей n - {x}')





