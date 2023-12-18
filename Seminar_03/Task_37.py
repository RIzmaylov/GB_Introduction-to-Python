# Задача №37. Решение в группах

# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).

# Input: 2 -> 3 4
# Output: 4 3

def reverse_print(N):
    if N == 0:
        return
    num = int(input())
    reverse_print(N - 1)
    print(num, end = ' ')

def reverse_print2(N):
    if N == 0:
        return ''
    num = int(input())
    return f'{reverse_print2(N - 1)} {num}'

N = int(input())
reverse_print(N)
print(reverse_print2(N))
    