# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# Пример:


# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

def my_pow(num, deg):
    if deg == 1:
        return num
    return num * my_pow(num, deg - 1)

a = 2
b = 3
print(my_pow(a, b))