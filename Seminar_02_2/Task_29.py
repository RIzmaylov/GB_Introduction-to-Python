# Задача №29. Решение в группах

# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

# Ваня:
# n = int(input())
# max_number = 1000         # 1) max_number = n
# while n != 0:             # 2) while n > 0 
#  n = int(input())
#  if max_number > n:       # 3) max_number < n
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:              # 1) while n > 0
#  n = int(input())         # 2) перенести после 30 строки
#  if max_number < n:
#  n = max_number           # 3) max_number = n
# print(n)                  # 4) print(max_number)
