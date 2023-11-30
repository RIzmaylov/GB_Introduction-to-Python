print(5)

number = int(input("Введите число: "))
print("Ваше число в кубе:", number ** 3)

for i in range(5):
    print(i)

if number % 5 == 0 and number % 2 == 0:
    print("Делится на 5 и на 2")
elif number % 5 == 0:
    print("Делится на 5")
elif number % 2 == 0:
    print("Делится на 2")
else:
    print("Не делится на 5 и 2")
