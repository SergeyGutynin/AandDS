# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

c1, c2, c3 = input('Введите трехзначное число: ')

r1 = int(c1) * int(c2) * int(c3)
print(f'Произведение цифр равно {r1}')

r2 = int(c1) + int(c2) + int(c3)
print(f'Сумма цифр равна {r2}')
