import numpy as np
from matplotlib import pylab, pyplot
import matplotlib.patches as patches
from math import sqrt
import matplotlib.pyplot as plt
import random
from collections import Counter


def random_Yi(a, b):
    size = random.randint(4, 10)
    size *= size
    size = 16
    arr = np.array([random.random() for i in range(size)], float)  # Ksi_i
    arr = np.dot(arr, b - a)
    arr = arr + a  # Xi
    arr = [pow(i, 4) for i in arr]  # Yi
    arr = np.around(arr,1)
    return arr


def draw_poligon(arr1, arr2):
    x = np.copy(arr2)
    y = sorted(list(set(arr1)))
    pylab.subplot(2, 2, 1)
    pylab.plot(x, y)
    pylab.title("Полигон распределения")


def draw_imper_func(arr1, arr2):
    relative_freq_arr = arr1 / len(arr2)
    # print("Относительные частоты:", relative_freq_arr)

    j = 0
    sum = 0
    summed_rel_freq = relative_freq_arr.copy()
    for i in range(relative_freq_arr.size):
        while i >= j:
            sum += relative_freq_arr[j]
            j += 1
        summed_rel_freq[i] = sum
        sum = 0
        j = 0
    # print("Относительные накопленные частоты:", summed_rel_freq)
    var_set_array = sorted(set(variation_series))
    var_set_array = np.concatenate([[-100], var_set_array, [var_set_array[len(var_set_array) - 1] + 100]])

    y = np.zeros(summed_rel_freq.size * 2)
    counter = 0
    k = 0
    for i in range(summed_rel_freq.size):
        y[k], y[k + 1] = summed_rel_freq[counter], summed_rel_freq[counter]
        k += 2
        counter += 1

    x = np.zeros(len(var_set_array) * 2)
    counter = 0
    k = 0
    for i in range(len(var_set_array)):
        if k + 2 == len(var_set_array) * 2:
            x[k], x[k + 1] = var_set_array[counter], var_set_array[counter] + 1
            continue
        x[k], x[k + 1] = var_set_array[counter], var_set_array[counter + 1]
        k += 2
        counter += 1

    y = np.concatenate([[0], y, [1]])
    y = np.concatenate([[0], y, [1]])

    pylab.subplot(2, 2, 2)
    pylab.plot(x, y)
    pylab.title("Эмпирическая функция")


def draw_equal_interval_hist(arr):
    arr1 = np.copy(arr)
    num_of_columns = sqrt(len(arr))
    print("Количество столбцов(равноинтервальный метод):", num_of_columns)
    columns_len = (arr[-1] - arr[-0]) / num_of_columns
    print("Длина интервала:", columns_len)
    columns_height = np.zeros(int(num_of_columns))

    right = arr[0] + columns_len
    k = 0
    for i in range(int(num_of_columns)):  # итерируемся M раз
        while True:
            if arr[k] <= right:
                columns_height[i] += 1
                k += 1
                if k == len(arr):
                    break
            else:
                right += columns_len
                break

    columns_height = columns_height.dot(1 / len(arr))
    print("Высоты столбцов(равноинтервальный метод):", columns_height)

    fig, ax = plt.subplots()
    # ax = pylab.subplots(2,2,3)
    arr = [i*columns_len for i in range(int(num_of_columns))]
    print(arr)
    for i in range(int(num_of_columns)):
        ax.add_patch(
            patches.Rectangle(
                (arr[i], 0),
                columns_len,
                columns_height[i],
                edgecolor="red"
            )
        )
    plt.xlim(-1, arr1[-1] + 10)


def draw_equal_chance_hist(arr):
    for i in arr:
        if i==0:
            arr = np.delete(arr, 0)
    num_of_columns = int(sqrt(len(arr)))
    num_of_elements_in_gap = int(len(arr)/num_of_columns)
    gap_lengths = np.zeros(int(num_of_columns)-1)
    gap_height = np.zeros(num_of_columns)
    print(num_of_columns)
    print(num_of_elements_in_gap)
    counter = 0
    print(sorted(list(set(arr) )))
    for i in range(int(num_of_columns)-1):
        gap_lengths[i] = (arr[counter+num_of_elements_in_gap-1]+arr[counter+num_of_elements_in_gap])/2 - arr[counter]
        counter += num_of_elements_in_gap
    gap_lengths = np.concatenate([[arr[0]], gap_lengths, [arr[-1]]])
    print(gap_lengths)

    for i in range(int(num_of_columns)):
        gap_height[i] = (1/num_of_columns)/(gap_lengths[i+1]-gap_lengths[i])


arr = random_Yi(-1, 3)
print("Исходный ряд:", )
variation_series = sorted(arr)
variation_series = np.around(variation_series)
print("Вариационный ряд:", variation_series)

frequency = Counter(variation_series)
freq_arr = np.array([frequency[i] for i in list(set(frequency.elements()))])
# print("Частоты:", freq_arr)

draw_poligon(variation_series, freq_arr)
draw_imper_func(freq_arr, arr)
draw_equal_interval_hist(variation_series)
#draw_equal_chance_hist(variation_series)
plt.show()
