# Определить, какое число в массиве встречается чаще всего.

import random


SIZE = 10
array = [random.randint(0, SIZE // 1.5) for _ in range(SIZE)]
print(array)

num = array[0]
max_frq = 1

for i in range(SIZE - 1):
    frq = 1
    for k in range(i + 1, SIZE):
        if array[i] == array[k]:
            frq += 1

    if frq > max_frq:
        max_frq = frq
        num = array[i]

if max_frq > 1:
    print(f'Число {num} встречается {max_frq} раз')
else:
    print('Все элементы уникальны')
