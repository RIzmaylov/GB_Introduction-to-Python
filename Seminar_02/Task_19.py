# Задача №19. Решение в группах

# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint

sizeList = int(input("Введите количество чисел в списке: "))
shift = int(input("Введите количество сдвигов вправо: "))

list1 = [randint(-10, 10) for _ in range(sizeList)]
print("Изначальный: ", list1)
list2 = []

for _ in range(shift):
    list1.append(list1.pop(0))
print("Сдвиг влево: ", list1)

# -------

for _ in range(shift):
    list1.insert(0, list1.pop())
print("Сдвиг вправо: ", list1)

# или

print("Используя срезы: ", list1[-shift:] + list1[:-shift])



