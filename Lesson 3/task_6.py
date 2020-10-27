# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.

import random


SIZE = 10
array = [random.randint(-100, 100) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0

for i in range (1, SIZE):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

print(array[idx_min], array[idx_max])

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

summ = 0

for i in range(idx_min + 1, idx_max):
    summ += array[i]

print(summ)