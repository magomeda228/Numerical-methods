import numpy as np
import matplotlib.pyplot as plt

# Задаем коэффициенты системы уравнений
A = np.array([
    [8, 4, 4],
    [4, 6, -1],
    [4, -2, 16]
])
b = np.array([10, 4, 4])

# Начальные значения
x = np.array([0.0, 0.0, 0.0])  # Начальная точка
tolerance = 1e-6  # Точность
max_iterations = 1000  # Максимальное число итераций
iteration_count = 0
x_history = [x.copy()]  # Для сохранения истории

# Итерационная формула
while iteration_count < max_iterations:
    x_new = np.zeros_like(x) # 0-евой массив тойже размерность что и x
    for i in range(len(x)):
        sum_ax = sum(A[i, j] * x[j] for j in range(len(x)) if j != i) # cумма всех членов a_ij * x_j кроме диагонального элемента
        x_new[i] = (b[i] - sum_ax) / A[i, i] #вычисление нового корня

    x_history.append(x_new.copy())
    # Проверка на сходимость
    if np.linalg.norm(x_new - x, ord=np.inf) < tolerance:
        break

    x = x_new
    iteration_count += 1

# Печать результата
print(f"Solution: {x_new}")
print(f"Number of iteration: {iteration_count}")

# Построение графика сходимости
x_history = np.array(x_history)
for i in range(len(x)):
    plt.plot(range(len(x_history)), x_history[:, i], label=f"x{i + 1}")

plt.xlabel("Iteration")
plt.ylabel("Value")
plt.title("Convergence of the simple iteration method")
plt.legend()
plt.grid()
plt.show()
