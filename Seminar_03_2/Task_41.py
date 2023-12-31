# Задача №41. Решение в группах

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.

# Ввод:                                 Ввод:
# 5                                     5
# 1 2 3 4 5                             1 5 1 5 1
# Вывод:                                Вывод:
# 0                                     2
# (каждое число вводится с новой строки)

from random import randint

N = int(input("Введите количество чисел в массиве: "))\

list1 = [randint(1, 10) for _ in range(N)]
print("Массив: ", list1)

cnt = 0
for i in range(1, N - 1):
    if list1[i - 1] < list1[i] > list1[i + 1]:
        cnt += 1

print("Кол-во элементов, удовлетворяющих условию: ", cnt)