# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 

num = int(input("Введите число: "))
cnt = 4
fib = 1
fib_res = 2

while num > fib_res:
    fib, fib_res = fib_res, fib + fib_res
    cnt += 1

if fib_res != num:
    print(-1)
else:
    print(cnt)