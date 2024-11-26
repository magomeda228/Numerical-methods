import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x ** 3

def true_integral(a, b):
    return (b ** 4) / 4 - (a ** 4) / 4

def rectangle_method(a, b, n):
    width = (b - a) / n
    area = sum(f(a + i * width) * width for i in range(n))
    return area

def trapezoidal_method(a, b, n):
    width = (b - a) / n
    area = (f(a) + f(b)) / 2
    for i in range(1, n):
        area += f(a + i * width)
    area *= width
    return area

def simpson_method(a, b, n):
    if n % 2 == 1:  # n должен быть четным
        n += 1
    width = (b - a) / n
    area = f(a) + f(b)

    for i in range(1, n):
        area += (4 if i % 2 != 0 else 2) * f(a + i * width)

    area *= width / 3
    return area

def compute_integrals(a, b, min_n, step_n, num_steps):
    n_values = np.arange(min_n, min_n + step_n * num_steps, step_n)
    results_rectangle = []
    results_trapezoidal = []
    results_simpson = []
    errors_rectangle = []
    errors_trapezoidal = []
    errors_simpson = []

    true_value = true_integral(a, b)

    for n in n_values:
        result_rectangle = rectangle_method(a, b, n)
        result_trapezoidal = trapezoidal_method(a, b, n)
        result_simpson = simpson_method(a, b, n)

        results_rectangle.append(result_rectangle)
        results_trapezoidal.append(result_trapezoidal)
        results_simpson.append(result_simpson)

        errors_rectangle.append(abs(result_rectangle - true_value))  # Истинная погрешность
        errors_trapezoidal.append(abs(result_trapezoidal - true_value))
        errors_simpson.append(abs(result_simpson - true_value))

    return n_values, results_rectangle, results_trapezoidal, results_simpson, errors_rectangle, errors_trapezoidal, errors_simpson, true_value

# Ввод параметров от пользователя
A = float(input("Введите левый край диапазона A: "))
B = float(input("Введите правый край диапазона B: "))
min_n = int(input("Введите минимальное число разбиений: "))
step_n = int(input("Введите шаг по числу разбиений: "))
num_steps = int(input("Введите число шагов: "))

# Вычисление интегралов
n_values, results_rectangle, results_trapezoidal, results_simpson, errors_rectangle, errors_trapezoidal, errors_simpson, true_value = compute_integrals(A, B, min_n, step_n, num_steps)

# Построение графика зависимости интеграла от количества разбиений
plt.figure(figsize=(12, 6))
plt.plot(n_values, results_rectangle, label='Метод прямоугольников', marker='o', linestyle='-')
plt.plot(n_values, results_trapezoidal, label='Метод трапеций', marker='x', linestyle='--')
plt.plot(n_values, results_simpson, label='Метод Симпсона', marker='s', linestyle='-.')
plt.axhline(y=true_value, color='r', linestyle='--', label='Истинное значение интеграла')
plt.title('Зависимость интеграла от количества разбиений')
plt.xlabel('Количество разбиений (n)')
plt.ylabel('Значение интеграла')
plt.legend()
plt.grid()
plt.ylim(min(min(results_rectangle), min(results_trapezoidal), min(results_simpson)) - 1e2,
         max(max(results_rectangle), max(results_trapezoidal), max(results_simpson)) + 1e2)  # Установка диапазона по оси Y
plt.show()

# Построение графиков истинной погрешности
plt.figure(figsize=(12, 6))
plt.plot(n_values, errors_rectangle, label='Истинная погрешность (Метод прямоугольников)', marker='o', linestyle='-')
plt.plot(n_values, errors_trapezoidal, label='Истинная погрешность (Метод трапеций)', marker='x', linestyle='--')
plt.plot(n_values, errors_simpson, label='Истинная погрешность (Метод Симпсона)', marker='s', linestyle='-.')

# Оценка погрешности по правилу Рунге
C_trapezoidal = (B - A) ** 4 / 12
C_simpson = (B - A) ** 5 / 180
C_rectangle = (B - A) ** 2 / 2
runge_errors_trapezoidal = [C_trapezoidal / n ** 2 for n in n_values]
runge_errors_simpson = [C_simpson / n ** 4 for n in n_values]
runge_errors_rectangle = [C_rectangle / n for n in n_values]

plt.plot(n_values, runge_errors_rectangle, label='Оценка погрешности (Метод прямоугольников)', linestyle='--', color='green')
plt.plot(n_values, runge_errors_trapezoidal, label='Оценка погрешности (Метод трапеций)', linestyle='--', color='orange')
plt.plot(n_values, runge_errors_simpson, label='Оценка погрешности (Метод Симпсона)', linestyle='--', color='green')

plt.title('Зависимость истинной погрешности от количества разбиений')
plt.xlabel('Количество разбиений (n)')
plt.ylabel('Истинная погрешность')
plt.legend()
plt.grid()
plt.ylim(0, max(max(errors_rectangle), max(errors_trapezoidal), max(errors_simpson)) )  # Установка диапазона по оси Y
plt.show()

# Вывод результата
print(f"Значения интеграла с использованием метода прямоугольников: {results_rectangle}")
print(f"Значения интеграла с использованием метода трапеций: {results_trapezoidal}")
print(f"Значения интеграла с использованием метода Симпсона: {results_simpson}")
print(f"Истинная погрешность (Метод прямоугольников): {errors_rectangle}")
print(f"Истинная погрешность (Метод трапеций): {errors_trapezoidal}")
print(f"Истинная погрешность (Метод Симпсона): {errors_simpson}")
