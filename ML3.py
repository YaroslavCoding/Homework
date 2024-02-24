import numpy as np

x1 = np.random.randint(100, size = 100)
x2 = np.random.randint(200, size = 100)
y = 3 * x1 + 2 * x2 - 1
x1 = x1 + np.random.randint(5, size = 100) / 10
x2 = x2 + np.random.randint(5, size = 100) / 10
y = y + np.random.randint(5, size = 100) / 10

epochs = 100
lr = 0.000045 #наиболее точно подобранный Learning rate
w1 = 0
w2 = 0
b = 0

for epoch in range(1, epochs+1):
    for i in range(len(x1)):
        y_predicted = w1 * x1[i] + w2 * x2[i] - b
        w1 = w1 + 2 * lr * x1[i] * (y[i] - y_predicted)
        w2 = w2 + 2 * lr * x2[i] * (y[i] - y_predicted)
        b = b + 2 * lr * (y[i] - y_predicted)

print(f"w1 = {w1}, w2 = {w2}, b = {b}")


