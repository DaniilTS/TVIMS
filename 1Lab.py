import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import random
from collections import Counter


def random_Yi(a, b):
    size = random.randint(100,1000)
    arr = np.array([random.random() for i in range(size)], float)  # Ksi_i
    arr = np.dot(arr, b - a)
    arr = arr + a  # Xi
    arr = [pow(i, 4) for i in arr]  # Yi
    arr = np.around(arr)
    return arr


arr = random_Yi(-1, 3)
print("Исходный ряд:", arr)
variation_series = sorted(arr)
variation_series = np.around(variation_series)
print("Вариационный ряд:", variation_series)

# Что во freq и зачем нужен set
frequency = Counter(variation_series)

print(frequency)
print(list(frequency.elements()))
freq_arr = np.array([frequency[i] for i in list(set(frequency.elements()))])
print("Частоты:", freq_arr)
print("Объём:", freq_arr.sum())

relative_freq_arr = freq_arr / len(arr)
print("Относительные частоты:", relative_freq_arr)

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
print("Относительные накопленные частоты:", summed_rel_freq)
var_set_array = sorted(set(variation_series))
var_set_array = np.concatenate([[-100], var_set_array, [var_set_array[len(var_set_array)-1]+100]])
print("Вариационный ряд без повторений(для определения промежутков):", var_set_array)

y_arr = np.zeros(summed_rel_freq.size * 2)
counter = 0
k = 0
for i in range(summed_rel_freq.size):
    y_arr[k], y_arr[k+1] = summed_rel_freq[counter], summed_rel_freq[counter]
    k += 2
    counter += 1

x_arr = np.zeros(len(var_set_array)*2)
counter = 0
k = 0
for i in range(len(var_set_array)):
    if k+2 == len(var_set_array)*2:
        x_arr[k], x_arr[k + 1] = var_set_array[counter], var_set_array[counter]+1
        continue
    x_arr[k], x_arr[k+1] = var_set_array[counter], var_set_array[counter+1]
    k += 2
    counter += 1

y_arr = np.concatenate([[0], y_arr, [1]])
y_arr = np.concatenate([[0], y_arr, [1]])

f = lambda xxx: (0.25*np.sqrt(np.sqrt(xxx))+0.25)
x = np.linspace(1, 81)

plt.xlim(-10, variation_series[len(arr)-1]+15), plt.ylim(0, 1.25)
plt.plot(x_arr, y_arr)
plt.plot(x, f(x))
plt.show()
