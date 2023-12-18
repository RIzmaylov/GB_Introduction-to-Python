# Задача №33. Решение в группах

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

import time

n = int(input("Введите количество оценок: "))

list_1 = [randint(1, 1000000) for _ in range(n)]

start_1 = time.time()

max_bal = max(list_1)
min_bal = min(list_1)
# print(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_bal:
        list_1[i] = min_bal
end_1 = time.time()
# print(list_1)

print(f"{end_1 - start_1}")

# 2
list_2 = [randint(1, 1000000) for _ in range(n)]

start_2 = time.time()

# print(list_2)

max_bal = min_bal = list_2[0]

for el in set(list_2):
    if el > max_bal:
        max_bal = el
    if el < min_bal:
        min_bal = el

for i in range(len(list_2)):
    if list_2[i] == max_bal:
        list_2[i] = min_bal

end_2 = time.time()

# print(list_2)

print(f"{end_2 - start_2}")

# 3
list_3 = [randint(1, 1000000) for _ in range(n)]

start_3 = time.time()

# print(list_3)

max_bal = min_bal = list_3[0]

list_max_bals = [0]

for i in range(len(list_3)):
    if list_3[i] > max_bal:
        max_bal = list_3[i]
        list_max_bals = [i]
    elif list_3[i] == max_bal:
        list_max_bals.append(i)
    if list_3[i] < min_bal:
        min_bal = list_3[i]

for i in list_max_bals:
    list_3[i] = min_bal

end_3 = time.time()

# print(list_3)

print(f"{end_3 - start_3}")