# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = int(input("Введите натуральное число: "))

digits = 1
even = 0
odd = 0

while num / (10 ** digits) >= 1:
    digits += 1

for ii in range(digits - 1, -1, -1):
    digit = num // (10 ** ii)

    if digit % 2:
        odd += 1
    else:
        even += 1

    num -= digit * (10 ** ii)

print(f"В числе {odd} нечетных и {even} четных цифр")
