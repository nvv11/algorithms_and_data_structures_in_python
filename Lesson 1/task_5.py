# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Номер буквы в алфавите (1-26): '))

num = ord('a') + num - 1

print(f'Это буква {chr(num)}')
