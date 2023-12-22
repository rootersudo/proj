import numpy as np
from scipy.integrate import solve_ivp


# Функция для решения задачи Коши
def solve_ivp_for_shooting(guess):
    def odefunc(x, y):
        return [y[1], x + y[0]]

    sol = solve_ivp(odefunc, [0, 1], [0, guess], t_eval=np.linspace(0, 1, 101))
    return sol.y[0][-1]  # Возвращаем значение y в конечной точке


# Функция для метода хорд
def chord_method(func, a, b, tolerance=1e-4, max_iterations=100):
    iteration = 0
    while iteration < max_iterations:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs(func(c)) < tolerance:
            return c
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iteration += 1
    return None


# Основная часть метода стрельбы
def shooting_method():
    tolerance = 0.01
    h = 0.01

    # Находим параметр "стрельбы" методом хорд
    guess_a = 1.0
    guess_b = 2.0
    param = chord_method(lambda guess: solve_ivp_for_shooting(guess), guess_a, guess_b, tolerance)

    # Решаем задачу Коши с найденным параметром
    def odefunc(x, y):
        return [y[1], x + y[0]]

    sol = solve_ivp(odefunc, [0, 1], [0, param], t_eval=np.linspace(0, 1, int(1 / h) + 1))

    return sol.t, sol.y[0]


# Получаем результат метода стрельбы
t, y = shooting_method()
print("Результат:")
for i in range(len(t)):
    print(f"y({t[i]:.2f}) = {y[i]:.6f}")