# Задача №17. Решение в группах

# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
from random import randint

sizeList = int(input("Введите количество чисел в списке: "))
list1 = []

for _ in range(sizeList):
    list1.append(randint(-10, 10))

# 14, 16, 17 строки можно заменить одной:
list2 = [randint(-10, 10) for _ in range(sizeList)]

print(list2)

print(len(set(list2)))



