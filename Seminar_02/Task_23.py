# Задача №23. Решение в группах

# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint
sizeList = int(input("Введите количество чисел в списке: "))

list1 = [randint(-10, 10) for _ in range(sizeList)]
print("Изначальный: ", list1)
cnt = 0
for i in range(sizeList - 1):
    if list1[i + 1] > list1[i]:
        cnt += 1

print(cnt)

# или

print(sum([1 for i in range(sizeList - 1) if list1[i + 1] > list1[i]]))