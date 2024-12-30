import numpy as np
import matplotlib.pyplot as plt

# Параметры
T0_1 = 100  # начальное значение T1
T0_2 = 0  # начальное значение T2
h = 1  # шаг по времени
t_end = 200  # конечное время
n_steps = int(t_end / h)  # количество шагов

# Массивы для хранения времени и значений T1, T2
t_values = np.linspace(0, t_end, n_steps + 1)
T1_values = np.zeros(n_steps + 1)
T2_values = np.zeros(n_steps + 1)
T1_values[0] = T0_1
T2_values[0] = T0_2

# Явная схема Эйлера
for n in range(n_steps):
    dT1_dt = 0.01 * (T2_values[n] - T1_values[n])
    dT2_dt = 0.01 * (T1_values[n] - T2_values[n])

    T1_values[n + 1] = T1_values[n] + h * dT1_dt
    T2_values[n + 1] = T2_values[n] + h * dT2_dt

# Построение графика
plt.plot(t_values, T1_values, label="T1(t)")
plt.plot(t_values, T2_values, label="T2(t)")
plt.xlabel("t, s")
plt.ylabel("Temperature")
plt.title("Solution of the system of equations using Euler's method")
plt.legend()
plt.grid(True)
plt.show()

