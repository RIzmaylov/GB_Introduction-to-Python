# Списки:

list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 5]
print(list_1) # [1, 2, 3, 5]
print(*list_1) # 1 2 3 5

for i in list_1:
    print(i)
print("--------------")
print(len(list_1)) # 4
print(list_1[3]) # 5
print(list_1[-1]) # 5

print("--------------")

# Добавление элемента:
list_1 = [1, 5]
print(list_1)
list_1.append(8)
print(list_1)

print("--------------")

#Удаление последнего элемента:
list1 = [12, 7, -1, 21, 0]
print(list1.pop()) # pop возвращает элемент
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)

print("--------------")

#Удаление конкретного элемента:
list1 = [12, 7, -1, 21, 0]
print(list1.pop(0)) # pop с аргументом 0 удаляет эл-нт с индексом 0
print(list1)

print("--------------")

#Добавление элемента в конкретную позицию:
list1 = [12, 7, -1, 21, 0]
print(list1.insert(2, 11)) # позиция и элемент вставки
print(list1) # [12, 7, 11, -1, 21, 0]

print("--------------")

#Срезы в списках:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[0])                 # 1
print(list1[1])                 # 1
print(list1[len(list1)-1])      # 10
print(list1[-5])                # 6
print(list1[:])                 # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[:2])                # [1, 2]
print(list1[len(list1)-2:])     # [9, 10]
print(list1[2:9])               # [3, 4, 5, 6, 7, 8, 9]
print(list1[6:-18])             # []
print(list1[0:len(list1):6])    # [1, 7]
print(list1[::6])               # [1, 7]

print("--------------")
print("--------------")

# Кортежи - это неизменяемый список, но работает быстрее:

t = ()

print(type(t)) # tuple

t = (1)
print(type(t)) # int, но:
t = (1, )
print(type(t)) # tuple, теперь правильный кортеж

print("--------------")

# преобразование списка в кортеж:

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

print("--------------")

# множественное присваивание:
a, b = 1, 2
a = b = 1
a, b, c = v

print (a, b, c)

# t = (1, 2)
# t[0] = 3 - ошибка! Изменять элементы нельзя!

print("--------------")
print("--------------")

# Словари - это неупорядоченные коллекции произвольных объектов с доступом по ключу:

d = {}
d = dict()
print(type(d))

d['q'] = 'qwerty'
print(d)
d['w'] = 'weasdasrty'
d['2'] = 'werwety'
d[34] = 55
print(d)
print(d['q'])

# print(d['typ'])  - ошибка - такого ключа не существует

print("--------------")
del d['w'] # удаление элемента
for item in d:
    print(item) # вывод только ключей

print("--------------")
for item in d:
    print('{}: {}'.format(item, d[item])) # вывод ключ - значение

for (k, v) in d.items():
    print(k, v) # вывод ключ - значение

print("--------------")
print("--------------")

# Множества содержат в себе уникальные элементы, но необязательно упорядоченные

colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}

colors.add('red')
print(colors) # {'red', 'green', 'blue'} только уникальные значения

colors.add('grey')
print(colors) # {'red', 'grey', 'green', 'blue'} 

colors.remove('grey')
print(colors) # {'red',, 'green', 'blue'} 
# colors.remove('grey') - ошибка, уже нет такого эл-та
colors.discard('grey') # проверяет перед удалением есть ли элемент, ошибки нет

colors.clear() # полное удаление
print(colors) # set()

# Операции со множествами:

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                    # c = {1, 2, 3, 5, 8}
u = a.union(b)                  # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b)           # i = {8, 2, 5}
dl = a.difference(b)            # dl = {1, 3}
dr = b.difference(a)            # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

print("--------------")

a = {1, 8, 6}

b = frozenset(a) # - создание замереженного множества, т.е. const
print(b) # frozenset({1, 8, 6})

print("--------------")
print("--------------")

# Генератор списка:

# Задача создать список из чисел от 1 до 100
# Обычный способ:
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1)
print("--------------")

# С помощью генератора списка:
list_2 = [i for i in range(1, 101)]
print(list_2)
print("--------------")

# С условием добавлять только четные числа:
list_3 = [i for i in range(1, 101) if i % 2 == 0]
print(list_3)
print("--------------")

# Допустим решили создать пары каждому из чисел (кортежи):
list_4 = [(i * 2, i ** 2) for i in range(1, 101) if i % 2 == 0]
print(list_4)
print("--------------")

