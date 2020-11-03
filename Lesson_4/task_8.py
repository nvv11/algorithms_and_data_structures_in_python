# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция
# нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность
# алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых
# уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под
# задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2


import cProfile


def prime(num):
    count = 1
    current_prime = 2

    while count < num:
        current_prime += 1
        for i in range(2, int(current_prime ** 0.5) + 1):
            if current_prime % i == 0:
                break
            else:
                count += 1

        return current_prime


def prime_sieve(num):
    assert num <= 5761455, 'Слишком большой аргумент'
    pi_func = {4: 10,
               25: 10 ** 2,
               168: 10 ** 3,
               1229: 10 ** 4,
               9592: 10 ** 5,
               78498: 10 ** 6,
               664579: 10 ** 7,
               5761455: 10 ** 8,
               }
    for key in pi_func.keys():
        if num <= key:
            size = pi_func[key]
            break

    array = [True for _ in range(size)]
    array[:2] = [False, False]
    count = 0

    for m in range(2, size):
        if array[m]:

            count += 1
            if count == num:
                return m

            for j in range(m ** 2, size, m):
                array[j] = False

    return None


cProfile.run('prime(100000)')
cProfile.run('prime_sieve(100000)')
