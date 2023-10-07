def rounding(): #округление
    x = float(input('Введите число:'))
    y = int(input('до скольки знаков округлить число:'))
    print(round(x, y))

def average(): #округление и среднее арифметическое
    x = float(input('введите число:'))
    y = float(input('введите число:'))
    print(round((x + y)/2))

x = (input('Какой режим хотите выбрать?')) #0 - округление, 1 - округление со средним арифметическим

if x == '0':
    rounding()

elif x == '1':
    average()

else:
    print("Допустимые значения только 0 и 1")

