# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных
# подстрок в этой строке.


def count_substring(s: str):

    set_hash = set()

    for i in range(len(s) - 1):
        for j in range(i + 1, len(s) + 1):
            set_hash.add(hash(s[i:j]))

    counter = len(set_hash) - 1
    return counter


my_str = input('Введите строку для проверки: ')
count = count_substring(my_str)
print(f'В строке "{my_str}" есть {count} различных подстрок')
