a = 'Python'
b = 'Hello World!'
z = 'Привет, меня зовут Вася'

print(a, b, z)
print(a, b, z, sep = ' \\\ ')               # смена разделителя, по умолчанию - пробел
print(a, b, z, end = ',')
print(a, b, z, end = ', ')                  # смена переноса строки на другой символ

print()
s = 'Python'

print(*s)          # -> print("P", 'y', 't', 'h', 'o', 'n')     сепарация контейнера на отдельные аргументы
print(*s, sep = '\n')

print()
print()

# Форматирование строк

name = "John"
print(f'Hi, {name}')                        # Hi, John
print('Hi, %s' % name)                      # Hi, John
print('Hi, {}'.format(name))                # Hi, John

print()
print()

# Работа со списками

my_list_1 = [123, 234, 456, 567, 5678]
print(f'{my_list_1 =}')
my_list_2 = my_list_1                    # Это не присваивание и создание ссылки на тот же лист!!!
print(f'{my_list_2 =}')

my_list_2[1] = 0
print(f'{my_list_1 =}')
print(f'{my_list_2 =}')

my_list_3 = my_list_1.copy()             # Это уже полное копирование
my_list_4 = my_list_1[:]                 # Аналогичная запись, тоже полное копирование (срез всего списка копируется)
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')
my_list_3[2] = 99999
print(f'{my_list_1 =}')
print(f'{my_list_3 =}')

# Вложенные списки
my_list1 = [123, 234, 345, 456, [123, 231, [123, 232, 3254], 324]]
my_list2 = my_list1.copy()               # Это полное копирование, но только верхнего списка. Все вложенные списки остаются ссылками!!!
print(f'{my_list1 =}')
print(f'{my_list2 =}')
my_list2[4][2][0] = 999
print(f'{my_list1 =}')
print(f'{my_list2 =}')

import copy                             # Для полного полного копирования нужно импортировать copy

my_list5 = copy.deepcopy(my_list1)
print(f'{my_list1 =}')
print(f'{my_list5 =}')
my_list5[4][2][0] = 'XXXX'
print(f'{my_list1 =}')
print(f'{my_list5 =}')

# Множественное присваивание

q, *w, e = (11, 22, 33, 44, 55)         # Если переменных меньше, чем значений, поставив * мы превратим элемент в список и все уйдет туда
print(q)
print(w)
print(e)
q, *w, e = (11, 55)         # Если переменных больше, чем значений, поставив * мы превратим элемент в пустой список
print(q)
print(w)
print(e)