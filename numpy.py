import numpy as np

print('------------------------------------------------')
print('Задача №1 и №2')
print('------------------------------------------------')

counter1 = 0 #счетчик результатов больше 7
counter2 = 0 #счетчик результатов всего

for i in range(1000):
    vector = np.random.randint(1, 10, size=100)
    vector_percentage = vector[vector > 7].size/vector.size*100 #находим процент в векторе
    if vector_percentage == 20.0:
        counter1 = counter1 + 1
    counter2 = counter2 + 1

result = counter1/counter2*100 #получаем, какая часть результатов равна 20% (получаем также в процентах)

print(result)
print('------------------------------------------------')
print('Задача №3,№4')
print('------------------------------------------------')

matrix = np.array(np.arange(1, 11))
matrix = np.resize(matrix, (10, 10))
print(matrix)
print('***********')
print(matrix.sum(0)) #сумма элементов матрицы в каждом столбце