def circle(r):
    return 2 *  3.14 * r * 2

def triangle(a, h):
    return a * h / 2

def rect(a, b):
    return a * b

def main():
    print('Начало работы модуля 1')

    print('Находим площадь сложной фигуры')
    area = rect(20, 30) + triangle(20, 15) - circle(5)
    print(f"{area = }")

    print('Завершение модуля 1')

if __name__ == '__main__':
    main() 