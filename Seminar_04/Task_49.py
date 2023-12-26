# Задача №49. Решение в группах

# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна

# Ввод:
orbits2 = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit2(orbits):
    not_circle = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    square = lambda orbit: orbit[0] * orbit[1] * 3.1415
    max_square = square(not_circle[0])
    res_index = 0
    for i in range(len(not_circle)):
        if square(not_circle[i]) > max_square:
            max_square = square(not_circle[i])
            res_index = i
    return not_circle[res_index]

print(*find_farthest_orbit2(orbits2))
# Вывод:
# 2.5 10

# 2

def find_farthest_orbit(orbits):
    not_circle = list(filter(lambda orbit: orbit[0] != orbit[1], orbits))
    squares = list(map(lambda orbit: orbit[0] * orbit[1], not_circle))
    max_square = max(squares)
    index_of_max = squares.index(max_square)
    return not_circle[index_of_max]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

print(*find_farthest_orbit(orbits))
    