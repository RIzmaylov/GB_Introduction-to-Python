def sum_numbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)

sum_numbers(5)

def sum_numbers2(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

print(sum_numbers2(5))

# Передача неограниченного количества аргументов
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'q', 'e', 'l'))

# Импорт модулей

import modul1
print(modul1.max1(5, 9))

# или

from modul1 import max1
print(max1(5, 9))

from modul1 import *        # - импорт всех функций из modul1

# или переименование модуля в программе для удобства использования

import modul1 as m1
print(m1.max1(5, 9))

# РЕКУРСИЯ

#  Фиббоначчи
def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n - 1) + fib(n - 2)

list1 = []
for i in range(1, 10):
    list1.append(fib(i))
print(list1)

#  Алгоритмы

# Быстрая сортировка

def quick_sort(array):
    if (len(array)) <= 1:
        return array
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14, 5 ,7 ,3, 34, 5, 123, 5, 43]))

# Сортировка слиянием

def merge_sort(nums):
    if (len(nums) > 1):
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [2, 54, 3, 323, 32, 3, 4, 234, 23, 34, 2, 1, 65, 74, 5]
merge_sort(list1)
print(list1)


