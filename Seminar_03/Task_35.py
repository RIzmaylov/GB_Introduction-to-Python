# Задача №35. Решение в группах

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)

# Input: 5
# Output: yes


def is_simple(num):
    if num != 2 and num % 2 == 0:
        return False
    for div in range(3, int(num ** 0.5) + 1, 2):
        if num % div == 0:
            return False
    return True

num = int(input("Введите число: "))

if is_simple(num):
    print("Число простое!")
else:
    print("Число не простое!")

