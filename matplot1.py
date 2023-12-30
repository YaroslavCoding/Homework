import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = input('График какой задачи вывести?')

if x == '1':

# задача №1
    def hyperbole(x): #функция гиперболы (другую не придумал), она самая гибкая
        y = 3 / x
        return y

    x = np.linspace(0, 3, 100)
    y = hyperbole(x)
    plt.plot(x, y, color='g', dashes=[5, 5], label='3 / x', alpha=0.4)

    x = np.linspace(-3, 0, 100)
    y = hyperbole(x)
    plt.plot(x, y, color='g', dashes=[5, 5], label='3 / x', alpha=0.4)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('Вот такая моя функция')
    plt.grid()

    plt.show()

elif x == '2':
    X = np.random.normal(0, 1, 3000)
    Y = np.random.normal(3, 4, 3000)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(X, Y, s=6, c=np.random.normal(0, 1, 3000), alpha=0.5, marker='o')
    plt.show()

elif x == '3':
    data = np.random.normal(16, 2, 1000)
    plt.hist(data, bins=30, color='r', alpha=0.5)
    plt.show()

