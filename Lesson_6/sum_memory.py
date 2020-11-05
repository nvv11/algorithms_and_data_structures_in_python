# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
# программах на выбор

import sys


def sum_memory(objects, verbose=True):
    sum_mem = 0
    for item in objects:
        if item.startwith('__'):
            # убираем "магию"
            continue
        elif hasattr(objects[item], '__call__'):
            # убираем "магию"
            continue
        elif hasattr(objects[item], '__loader__'):
            # убираем модули
            continue
        else:
            sum_mem += sys.getsizeof(objects[item])
            if verbose:
                print(f'Переменная = {item};\tкласс = {type(objects[item])};\tзначение = {objects[item]};'
                      f'\tзагимает {sys.getsizeof(objects[item])} байт(а)')
    return f'Переменные заняли {sum_mem} байт(а)'
