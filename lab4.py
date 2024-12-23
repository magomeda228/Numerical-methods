import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a = input('Graph with error (g/G) or Method(m/M)?')
if (a=='g' or a=='G'):
    I_data = [
        [100, 50, 25, 10, 5, 2, 1],
        [116, 303, 411, 478, 500, 514, 519],
        [680, 552, 530, 524, 523, 523, 523],
        [680, 524, 530, 524, 524, 523, 523],
        [526, 524, 523, 523, 523, 523, 523],
        [782, 586, 521, 526, 523, 523, 523],
        [546, 518, 524, 523, 523, 523, 523],
        [526, 523, 525, 523, 534, 523, 523],
        [655, 536, 525, 524, 523, 523, 523],
        [520, 523, 523, 523, 523, 523, 523]
    ]
    I_data_2 = [
        [4970,	5602,	5602,	5543,	5648,	5562,	5543,	5554,	5544], # tau = 100
        [7050,	7485,	7485,	7445,	7485,   7485,	7445,	7448,	7447], # tau = 50
        [9418,	9427,	9427,	9427,	9427,	9427,	9427,	9427,	9427], # tau = 10
        [9705,	9709,	9709,	9709,	9709,	9709,	9709,	9709,	9709]  # tau = 5
    ]
    T0 = 10000
    t = 100
    m = 0.0059
    for i in range(len(I_data)-1):
        for j in range(len(I_data[i])):
            I_data[i+1][j] -= T0 * np.exp( -m * 500)

    p = np.array([1, 2, 2, 4, 2, 2, 4, 4, 4])
    Runge_100_50 = np.abs(np.array(I_data_2[0]) - np.array(I_data_2[1])) / (2 ** p - 1)
    Runge_10_5 = np.abs(np.array(I_data_2[2]) - np.array(I_data_2[3])) / (2 ** p - 1)

    Runge = np.vstack([Runge_100_50, Runge_10_5])
    error = [
        [-407,	157,	157	,3	,259	,23	,3	,132	,-3],
        [-220,	29,	1,	1,	63,	-5,	-0.51,	13,	-0.56],
        [-112,	7,	7,	-0.58,	-2,	1,	2,	2,	-0.47],
        [-45,	1,	1,	-0.45,	3,	-0.45,	-0.45,	1,	-0.45],
        [-23,	-0.41,	1,	-0.41,	-0.41,	-0.41,	-0.41,	-0.41,	-0.41],
        [-9,	-0.39,	-0.36,	-0.39,	-0.38,	-0.39,	-0.37,	-0.35,	-0.39],
        [-4,	-0.35,	-0.39,	-0.36,	-0.39,	-0.37,	-0.39,	-0.36,	-0.39]
    ]

    x = [100, 50, 25, 10, 5, 2, 1]
    x2 = [50, 5]
    fig, ax = plt.subplots(1, 9, figsize=(50, 7))

    name= ['ЯЭ',	'МЭ',	'ИЭ',	'РК4',	'ЯА2',	'ПК2',	'ПК4',	'Г',	'АМ']
    for j in range(9):
        ax[j].plot(x, np.abs(np.array(error)[:, j]))
        ax[j].plot(x2, Runge[:, j], 'o')
        ax[j].set_xlabel(f"tau \n {name[j]}")
        ax[j].set_ylabel('Error')
        ax[j].grid(True, linestyle='--', alpha=0.7)
        ax[j].set_xticks(x)
        ax[j].set_xscale('log')
        ax[j].get_xaxis().set_major_formatter(plt.ScalarFormatter())
    fig.suptitle('All error')
    plt.tight_layout(pad = 3.0)
    plt.show()
else:
    # Параметры задачи
    T0 = 10000  # Начальное значение температуры
    k = 0.0059  # Коэффициент
    h = 1  # Шаг времени
    t_end = 500  # Конечное время

    # Инициализация
    t_values = np.arange(0, t_end + h, h)  # Временные шаги
    T_values = np.zeros_like(t_values)  # Массив для хранения решения
    T_values[0] = T0  # Начальное услови

    # Метод Эйлера
    for n in range(len(t_values) - 1):
        T_values[n + 1] = T_values[n] - h * k * T_values[n]

    # Аналитическое решение для сравнения
    T_exact = T0 * np.exp(-k * t_values)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, T_values, label='Явная схема Эйлера', linestyle='--')
    plt.plot(t_values, T_exact, label='Аналитическое решение', linewidth=2)
    plt.xlabel('Время, t')
    plt.ylabel('Температура, T')
    plt.title('Решение уравнения dT/dt = -0.0059T методом Эйлера')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
