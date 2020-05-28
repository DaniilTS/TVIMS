import numpy as np
from matplotlib import pylab, pyplot
import matplotlib.patches as patches
from math import sqrt
import matplotlib.pyplot as plt
import random
import math


def random_Yi(a, b):
    size = random.randint(80, 150)
    print(size)
    size = 16

    arr = np.array([a + random.random() * (b - a) for i in range(size)], float)  # Ksi_i
    arr = [pow(i, 4) for i in arr]  # Yi
    arr = sorted(arr)
    arr = np.around(arr, 1)
    return arr


def plot_equal_interval_hist(variation_series, num_of_columns, A, B):
    len_of_row = variation_series[-1] - variation_series[0]
    print("Длина ряда", len_of_row)
    len_of_column = len_of_row / num_of_columns
    print("Ширина столбцов:", len_of_column)

    sum = 0
    for i in range(num_of_columns):
        A[i] = sum
        B[i] = A[i] + len_of_column
        sum += len_of_column

    columns_height = np.zeros(num_of_columns)
    j = 0
    for i in variation_series:
        if i == B[j] and i != variation_series[-1]:
            columns_height[j] += 0.5
            columns_height[j + 1] += 0.5
            j += 1
            continue
        elif A[j] <= i <= B[j]:
            columns_height[j] += 1
        else:
            if j == len(columns_height)-1:
                break
            columns_height[j + 1] += 1
            j += 1

    columns_height /= len(variation_series)

    print("Высоты столбцов", columns_height)
    print(np.sum(columns_height))
    fig, ax = plt.subplots()
    for i in range(int(num_of_columns)):
        ax.add_patch(
            patches.Rectangle(
                (A[i], 0),
                len_of_column,
                columns_height[i],
                edgecolor="red",
            )
        )

    f = lambda x: (1 / (16 * np.power(x, 3 / 4)))
    x = np.linspace(0.0005, 81)
    plt.plot(x, f(x), "yellow")
    plt.xlim(-1, variation_series[-1] + 1)
    plt.ylim(0, 1)
    plt.show()
    return A, B


def plot_poligon_and_func(A, B, num_of_columns, variation_series):
    x = np.zeros(num_of_columns)
    for i in range(num_of_columns):
        x[i] = A[i] + (B[i] - A[i]) / 2

    y = np.zeros(num_of_columns)
    uniq = []
    j = 0
    for i in variation_series:
        if A[j] <= i <= B[j]:
            if i not in uniq:
                y[j] += 1
                uniq.append(i)
        else:
            j += 1
            uniq.append(i)
            y[j] += 1
    y /= len(variation_series)

    pylab.subplot(1, 1, 1)
    pylab.ylim(-0.1, y[0]+0.05)
    pylab.xlim(-2, x[-1] + 5)
    pylab.plot(x, y)
    f = lambda x: (1 / (16 * np.power(x, 3 / 4)))
    x = np.linspace(0.000005, 81)
    pylab.plot(x, f(x), "yellow")
    x, y = [-100, 0],[0, 0]
    pylab.plot(x, y, "yellow")
    x, y = [81, 100], [0, 0]
    pylab.plot(x, y, "yellow")
    plt.show()


def plot_equal_chance_hist(M):
    while True:
        if len(variation_series) % M == 0:
            num_of_elements_on_interval = int(len(variation_series) / M)
            if num_of_elements_on_interval == variation_series[-1]:
                M += 2
            elif variation_series[int(num_of_elements_on_interval) + 1] == 0:
                M -= 1
            else:
                break
        else:
            M -= 1

    print("Количество элементов на интервале:", int(num_of_elements_on_interval))
    num_of_columns = int(len(variation_series) / num_of_elements_on_interval)
    print("Количество столбцов:", num_of_columns)

    A = np.zeros(num_of_columns)
    B = np.zeros(num_of_columns)
    j = num_of_elements_on_interval
    for i in range(len(A)):
        B[i] = (variation_series[j] + variation_series[j + 1]) / 2
        if i == 0:
            A[i] = variation_series[0]
        else:
            A[i] = B[i - 1]
        j += num_of_elements_on_interval
        if j == len(variation_series):
            A[i + 1] = B[i]
            B[i + 1] = variation_series[-1]
            break
    print(A)
    print(B)

    column_heights = np.zeros(num_of_columns)
    column_len = np.zeros(num_of_columns)
    for i in range(num_of_columns):
        column_heights[i] = num_of_elements_on_interval / (len(variation_series) * (B[i] - A[i]))
        column_len[i] = B[i] - A[i]
    print("Высоты столбцов:", column_heights)

    fig, ax = plt.subplots()
    for i in range(int(num_of_columns)):
        ax.add_patch(
            patches.Rectangle(
                (A[i], 0),
                column_len[i],
                column_heights[i],
                edgecolor="red",
            )
        )
    f = lambda x: (1 / (16 * np.power(x, 3 / 4)))
    x = np.linspace(0.0005, 81)
    plt.plot(x, f(x), "yellow")
    plt.xlim(-1, variation_series[-1] + 1)
    plt.ylim(0, column_heights[0] + 0.05)
    plt.show()


source_row = random_Yi(-1, 3)
variation_series = sorted(source_row)
print("Вариационный ряд:", variation_series)

if len(variation_series) <= 100:
    M = int(sqrt(len(variation_series)))
else:
    M = int(random.randint(2, 4) * math.log(len(variation_series),10))

print("@@@@@@@@@@ РАВНОИНТЕРВАЛЬНЫЙ МЕТОД @@@@@@@@@")
print("количество столбцов:", M)
A = np.zeros(M)
B = np.zeros(M)
A, B = plot_equal_interval_hist(variation_series, M, A, B)
plot_poligon_and_func(A, B, M, variation_series)

print("@@@@@@@@@@ РАВНОВЕРОЯТНОСТНЫЙ МЕТОД @@@@@@@@@")
plot_equal_chance_hist(M)
