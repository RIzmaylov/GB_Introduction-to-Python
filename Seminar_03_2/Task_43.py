# Задача №43. Решение в группах

# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод:                     Вывод:
# 1 2 3 2 3 2 2                7

from random import randint

N = int(input("Введите количество чисел в массиве: "))\

list1 = [randint(1, 10) for _ in range(N)]
print("Массив: ", list1)

cnt = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if list1[i] == list1[j]:
            cnt += 1

print("Кол-во пар: ", cnt)

# 2

cnt = 0
for i in range(N - 1):
    cnt += list1[i + 1:].count(list1[i])

print("Кол-во пар: ", cnt)
