# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random

num = random.randint(0, 100)

print("Сгенерировано случайное число от 0 до 100.\n"
      "У Вас есть 10 попыток, что бы его отгадать.")

for count in range(1, 11):
    user_num = int(input(f"Попытка {count:2}. Введите число от 0 до 100: "))

    if num == user_num:
        print(f"Вы угадали число {num}")
        break
    elif num > user_num:
        print(f"Сгенерированное число больше {user_num}")
    elif num < user_num:
        print(f"Сгенерированное число меньше {user_num}")

    if count == 10:
        print(f"Вам не удалось отгадать число {num}")
