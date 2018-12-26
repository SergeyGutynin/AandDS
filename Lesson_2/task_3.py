# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран
# Например, если введено число 3486, то надо вывести число 6843.

num = int(input("Введите натуральное число: "))

digits = 1
out_num = 0

while num / (10 ** digits) >= 1:
    digits += 1

for ii in range(digits - 1, -1, -1):
    digit = num // (10 ** ii)

    out_num += digit * (10 ** (digits - 1 - ii))

    num -= digit * (10 ** ii)

print(f"Обратное по порядку цифр число {out_num}")
