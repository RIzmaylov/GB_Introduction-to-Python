# Задача №25. Решение в группах

# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

text = " a a a b c a a d c d d"

list_symbols = text.split()

print(list_symbols)

uniq_symbols = dict()

for symbol in list_symbols:
    if symbol not in uniq_symbols:
        uniq_symbols[symbol] = 0
        print(symbol, end = ' ')
    else:
        uniq_symbols[symbol] += 1
        print(f"{symbol}_{uniq_symbols[symbol]}", end = ' ')

# 2 ________________________________________________

text2 = " a a a b c a a d c d d"

list_symbols2 = text2.split()
print()
print()
print(list_symbols2)

uniq_symbols2 = dict()
result = ''

for symbol in list_symbols2:
    if symbol not in uniq_symbols2:
        uniq_symbols2[symbol] = 0
        result += symbol + ' '
    else:
        uniq_symbols2[symbol] += 1
        result += f"{symbol}_{uniq_symbols2[symbol]} "

print(result.strip())

# 3 ________________________________________________

text3 = " a a a b c a a d c d d"

list_symbols3 = text3.split()
print()
print()
print(list_symbols3)

uniq_symbols3 = dict()
result2 = ''

for symbol in list_symbols3:
    if symbol not in uniq_symbols3:
        result2 += f'{symbol} '
    else:
        result2 += f"{symbol}_{uniq_symbols3[symbol]} "
    uniq_symbols3[symbol] = uniq_symbols3.get(symbol, 0) + 1

print(result.strip())

