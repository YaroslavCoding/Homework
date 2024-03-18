import scipy

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=30)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)
model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)

print(f'MSE - {mse}')

plt.figure(figsize=(10, 5))
plt.scatter(x_train, y_train, color='green', label='Набор обучения')
plt.scatter(x_test, y_test, color='red', label='Набор тестирования')

plt.plot(x_test, y_pred, color='red', label='Линейная регрессия')
plt.xlabel('Признак')
plt.ylabel('Целевое значение')
plt.title('Линейная регрессия с обучающими и тестовыми наборами')
plt.legend()
plt.grid(True)
plt.show()