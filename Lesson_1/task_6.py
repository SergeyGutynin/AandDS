# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

num = int(input('Введите номер буквы в алфавите (от 1 до 26): '))

if 1 <= num <= 26:
    c = chr(ord('a') + num - 1)
    print(f'Соответствующая буква в алфавите {c}.')
else:
    print('Значение должно быть в интервале от 1 до 26.')
