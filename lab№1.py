import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """Целевая функция f(x) = 4x - ln(x) - 5."""
    if x <= 0:
        raise ValueError("Function is undefined for x <= 0 due to ln(x).")
    return 4 * x - math.log(x) - 5

def bisection_method(a, b, tol=1e-6, max_iter=100):
    """Метод половинного деления (бисекции)."""
    if a <= 0 or b <= 0:
        raise ValueError("Boundary values a and b must be greater than 0 due to ln(x) in the function.")
    if f(a) * f(b) > 0:
        print("На отрезке [a, b] нет корней или их количество четное.")
        return None, []
    iterations = []
    for i in range(max_iter):
        c = (a + b) / 2.0
        iterations.append(f(c))  # Сохраняем значение функции
        if abs(f(c)) < tol or abs(b - a) < tol:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    print("Решение не найдено за указанное количество итераций.")
    return None, iterations

def simple_iteration(g, x0, tol=1e-6, max_iter=100):
    """Метод простой итерации."""
    iterations_x = [x0]  # Список для хранения значений x
    for i in range(max_iter):
        x_next = g(x0)  # Вычисляем следующее значение x

        # Сохраняем текущее значение x
        iterations_x.append(x_next)

        # Проверка на расходимость
        if abs(x_next - x0) > 2 * abs(x0):  # Условие для расходимости
            print("Итерации расходятся. Попробуйте изменить начальное приближение или функцию g(x).")
            return None, iterations_x

        # Проверка на сходимость
        if abs(x_next - x0) < tol:
            return x_next, iterations_x

        x0 = x_next  # Обновляем x0 для следующей итерации

    print("Решение не найдено за указанное количество итераций.")
    return None, iterations_x

# Example transformation function for f(x) = 0
g = lambda x: np.exp((np.log(x) + 5) / 4)  # Преобразование f(x) = 0 в x = g(x)


def newton_raphson(x0, tol=1e-6, max_iter=100):
    """Метод Ньютона-Рафсона."""

    def f_derivative(x):
        return 4 - 1 / x  # Производная f(x)

    iterations_x = [x0]  # Сохраняем значения x
    for i in range(max_iter):
        fx = f(x0)
        f_prime_x = f_derivative(x0)

        if abs(f_prime_x) < tol:
            print("Производная близка к нулю, метод может не сойтись.")
            return None, iterations_x

        x_next = x0 - fx / f_prime_x
        iterations_x.append(x_next)  # Сохраняем значение x для графика

        if abs(x_next - x0) < tol:
            return x_next, iterations_x

        x0 = x_next

    print("Решение не найдено за указанное количество итераций.")
    return None, iterations_x

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    """Метод секущих с проверкой на равенство значений функции на границах интервала."""
    if f(x0) * f(x1) > 0:
        print(f"Ошибка: f({x0}) и f({x1}) имеют одинаковый знак. На отрезке [{x0}, {x1}] нет корней.")
        return None, []

    iterations = []
    for i in range(max_iter):
        if abs(f(x1) - f(x0)) < tol:
            print("Разделение на ноль, метод не может продолжаться.")
            return None, iterations
        x_next = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations.append(f(x_next))  # Сохраняем значение функции
        if abs(x_next - x1) < tol:
            return x_next, iterations
        x0, x1 = x1, x_next
    print("Решение не найдено за указанное количество итераций.")
    return None, iterations

def chord_method(a, b, tol=1e-6, max_iter=100):
    """Метод хорд с проверкой на равенство значений функции на границах интервала."""
    if f(a) * f(b) > 0:
        print(f"Ошибка: f({a}) и f({b}) имеют одинаковый знак. На отрезке [{a}, {b}] нет корней.")
        return None, []

    iterations = []
    for i in range(max_iter):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        iterations.append(f(c))  # Сохраняем значение функции
        if abs(f(c)) < tol or abs(b - a) < tol:
            return c, iterations
        a, b = b, c  # Обновляем границы интервала
    print("Решение не найдено за указанное количество итераций.")
    return None, iterations

def idrichli_method(x0, x1, tol=1e-6, max_iter=100):
    """Метод идрихле с проверкой на равенство значений функции на границах интервала."""
    if f(x0) * f(x1) > 0:
        print(f"Ошибка: f({x0}) и f({x1}) имеют одинаковый знак. На отрезке [{x0}, {x1}] нет корней.")
        return None, []

    iterations = []
    for i in range(max_iter):
        x_next = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        iterations.append(f(x_next))  # Сохраняем значение функции
        if abs(x_next - x1) < tol:
            return x_next, iterations
        x0, x1 = x1, x_next
    print("Решение не найдено за указанное количество итераций.")
    return None, iterations

def plot_iterations(iterations_x, method_name):
    """Функция для построения графика."""
    plt.plot(range(len(iterations_x)), iterations_x, marker='o')
    plt.title(f'Значения x от итерации ({method_name})')
    plt.xlabel('Итерация')
    plt.ylabel('x')
    plt.axhline(0, color='gray', linestyle='--')  # Линия y=0 для справки
    plt.grid()
    plt.show()

def main():
    print("Выберите метод решения уравнения f(x) = 4x - ln(x) - 5 = 0")
    print("1: Метод половинного деления")
    print("2: Метод простой итерации")
    print("3: Метод Ньютона-Рафсона")
    print("4: Метод секущих")
    print("5: Метод хорд")
    print("6: Метод Риддерае")
    choice = int(input("Введите номер метода (1-6): "))

    if choice == 1:
        a = float(input("Введите начальное значение интервала a: "))
        b = float(input("Введите конечное значение интервала b: "))
        result, iterations = bisection_method(a, b)
        method_name = "Метод половинного деления"

    elif choice == 2:
        x0 = float(input("Введите начальное приближение x0: "))
        g = lambda x: (math.exp(4 * x - 5))  # Преобразование f(x) = 0 в x = g(x)
        result, iterations = simple_iteration(g, x0)
        method_name = "Метод простой итерации"

    elif choice == 3:
        x0 = float(input("Введите начальное приближение x0: "))
        result, iterations = newton_raphson(x0)
        method_name = "Метод Ньютона-Рафсона"

    elif choice == 4:
        x0 = float(input("Введите начальное приближение x0: "))
        x1 = float(input("Введите начальное приближение x1: "))
        result, iterations = secant_method(x0, x1)
        method_name = "Метод секущих"

    elif choice == 5:
        a = float(input("Введите начальное значение интервала a: "))
        b = float(input("Введите конечное значение интервала b: "))
        result, iterations = chord_method(a, b)
        method_name = "Метод хорд"

    elif choice == 6:
        x0 = float(input("Введите начальное приближение x0: "))
        x1 = float(input("Введите начальное приближение x1: "))
        result, iterations = idrichli_method(x0, x1)
        method_name = "Метод идрихле"

    else:
        print("Некорректный ввод. Пожалуйста, выберите 1-6.")
        return

    if result is not None:
        print(f"Корень уравнения: x ≈ {result} найден.")
    else:
        print("Решение не удалось найти.")
    plot_iterations(iterations, method_name)


if __name__ == "__main__":
    main()
