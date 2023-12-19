# Задача №45. Решение в группах

# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105

# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).

# Ввод:                 Вывод:
# 300                   220 284

def sum_divs(num):
    res_sum = 1
    for div in range(2, int(num ** 0.5)):
        if num % div == 0:
            res_sum += div + num // div
    return res_sum

size = int(input("Введите предельное число: "))

first_num = second_num = 0

for num1 in range(size - 1):
    for num2 in range(num1 + 1, size):
        if sum_divs(num1) == num2 and sum_divs(num2) == num1:
            first_num = num1
            second_num = num2

print(first_num, second_num)

# 2

for num1 in range(size - 1):
    num2 = sum_divs((num1))
    if sum_divs(num2) == num1 and num1 < num2:
        print(num1, num2)

