import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dat50 = [[10000, 7050, 4970, 3504, 2470, 1741, 1227.8, 866, 610, 430, 303],
        [10000, 7485, 5602, 4193, 3193, 2349, 1758, 1316, 985, 736, 552],
        [10000, 7485, 5602, 4193, 3139, 2349, 1758, 1316, 985, 737, 552],
        [10000, 7446, 5544, 4127, 3073, 2288, 1704, 1268, 944, 703, 524]]
dat100 = [
        [10000, 4100, 1681, 689, 282, 116],
        [10000, 5840, 3411, 1992, 1164, 680],
        [10000, 5840, 3411, 1992, 1163, 680],
        [10000, 5548, 3078, 1708, 948, 526],
        ]

m = -0.0059
T0 = 10000
T_50 = np.linspace(0, 500, 11)
T_100 = np.linspace(100, 500, 5)
# local_error_t_50 = np.abs(np.diff(np.array(dat50)))
# local_error_t_100 = np.abs(np.diff(np.array(dat100)))
# error_t_50 = np.abs(np.array(dat50) - T0 * np.exp(  m * T_50))
# error_t_100 = np.abs(np.array(dat100) - T0 * np.exp(  m * T_100))
# p = [[1], [2], [2], [4]]

# trimmed_dat100 = np.delete(np.array(dat100)[:, 1:5], 2, axis=1)
# runge_100 = np.abs(np.diff(trimmed_dat100, axis=1)) / (2 ** np.array(p) -1 )
# print(np.delete(np.array(dat100)[:,1:5],2),'\n')
# dat50_trimmed = np.delete(np.array(dat50)[:, 1:5], 3, axis=1)
# runge_50 = np.abs(np.diff(dat50_trimmed, axis=1)) / (2 ** np.array(p) - 1)
runge = np.array([ [870, 789, 534, 528],
          [79, 73, 78, 60],
          [79, 73, 78, 60],
          [0.26, 0.33, 0.26, 0.13]
])
loc_error = np.array([
    [870, 432, 216, 106, 53],
    [238, 79, 107, 42, 23],
    [238, 79, 107, 42, 23],
    [4, 3, 0.7, 0.6, 0.2]
])
# # Преобразуем runge_100 в двумерный массив для корректной индексации
# runge_100 = runge_100.reshape((len(dat100), -1))
# print(runge_100)
# print(np.abs(np.diff(np.array(dat50))))
# print(np.abs(np.diff(np.array(dat100))))
# print(np.abs(np.array(dat50) - T0 * np.exp(  m * T1)))
# print(np.abs(np.array(dat100) - T0 * np.exp(  m * T2)))
name=['ЯЭ','МЭ','ИЭ','РК4']
comand_check = input('Graph(g/G) or Callculation?(c/C): ')
if comand_check in ['g', 'G']:
        # #Локальная погрешность t=100
        # for j in range(loc_error.shape[0]):
        #         sns.lineplot(x=T_100, y=loc_error[j], marker='o',label=name[j])
        #         plt.title("Local error, delta T = 100 s")
        #         plt.xlabel("t, s")
        #         plt.ylabel("Delta T")
        #         plt.grid(True, linestyle='--', alpha=0.7)
        # plt.show()
        #Сравнение локальной погершнотси и
        for j in range(loc_error.shape[0]):
                sns.lineplot(x=T_100, y=loc_error[j], marker='o',label=f"{name[j]} Local")
        for j in range(runge.shape[0]):
                sns.lineplot(x=T_100[:4], y=runge[j], marker='o',label=f"{name[j]} Runge")
        plt.title("Comparing error, delta T = 100 s")
        plt.xlabel("t, s")
        plt.ylabel("Delta T")
        plt.yscale('log')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()
        #
        # for j in range(local_error_t_50.shape[0]):
        #         sns.lineplot(x=T_50[1:], y=local_error_t_50[j], marker='o',label=f"{name[j]} Local")
        # for j in range(runge_50.shape[0]):
        #         sns.lineplot(x=[100, 200], y=runge_50[j], marker='o',label=f"{name[j]} Runge")
        # plt.title("Comparing error, delta T = 50 s")
        # plt.xlabel("t, s")
        # plt.ylabel("Delta T")
        # plt.grid(True, linestyle='--', alpha=0.7)
        # plt.grid(True, linestyle='--', alpha=0.7)
        # plt.show()
elif comand_check in ['c', 'C']:
        #Данные
        h = 1  # Шаг по времени
        T0 = 10000  # Начальное значение температуры
        t_max = 500  # Максимальное время

        # Инициализация времени и температур
        t_values = np.arange(0, t_max + h, h)
        T_values = np.zeros(len(t_values))

        # Условие на начальное значение
        T_values[0] = T0

        # Модифицированная схема Эйлера для первого шага
        T_predict = T_values[0] - h * (0.0059) * T_values[0]
        # Корректировка (усреднение наклонов)
        T_values[1] = T_values[0] - h * (0.0059) * (T_values[0] + T_predict) / 2

        # Явная схема Алмса второго порядка для последующих шагов
        for n in range(1, len(t_values) - 1):
            T_values[n + 1] = T_values[n] + h * (1.5 * (-0.0059 * T_values[n]) - 0.5 * (-0.0059 * T_values[n - 1]))

        # Визуализация результата
        plt.plot(t_values, T_values, label="Temperature T(t)")
        plt.title("Solution of dT/dt = -0.059T using 2nd Order Adams-Bashforth Scheme")
        plt.xlabel("Time (t)")
        plt.ylabel("Temperature (T)")
        #plt.yscale('log')
        plt.grid(True)
        plt.legend()
        plt.show()