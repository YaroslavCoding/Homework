x = [1, 3, 7]
y = [2, 6, 4]

w = 0
b = 0

lr = 0.01
loss = 0

loss_tendency = []
w_and_b = []

for i in range(0, len(x)):
    y_predicted = w * x[i] + b
    loss = y[i] - y_predicted
    loss_tendency.append(loss)
    w = w + 2 * lr * x[i] * loss
    w_and_b.append(w)
    b = b + 2 * lr * loss
    w_and_b.append(b)
    w_and_b.append("|")

print(f"Изменение коэффициентов потери: {loss_tendency}")
print(f"Соответствующие коэффициенты: {w_and_b}")

#Вывод: веса w = 0.545856 и b = 0.179008 получились похожими на настоящие, так как имеют наименьший коэффициент потери - 1.1104000000000003


