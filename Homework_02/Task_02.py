# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

# Пример:


list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
diff = abs(abs(list_1[0]) - abs(k))
res_num = list_1[0]

for elem in list_1:
    if abs(abs(elem) - abs(k)) < diff:
        diff = abs(abs(elem) - abs(k))
        res_num = elem
print(res_num)

