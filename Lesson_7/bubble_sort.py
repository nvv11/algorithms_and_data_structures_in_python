# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран
# исходный и отсортированный массивы.

import random


def bubble_sort(array, reverse=False):

    sing = int(reverse) * 2 - 1
    pos = 1

    while pos < len(array):
        is_sorted = True

        for i in range(len(array) - pos):
            if array[i] * sing < array[i + 1] * sing:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted =  False

        if is_sorted:
            break

        pos += 1


SIZE = 32
LIMIT = 100
data = [random.randrange(-LIMIT, LIMIT) for i in range(SIZE)]
print(data)
bubble_sort(data, reverse=True)
print(data)
