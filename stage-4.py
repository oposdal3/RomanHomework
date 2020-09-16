def my_func(number, place):
    for i in range(place * -1 - 1):
        number *= number
    print(round(1 / number, 2))


while True:
    try:
        a = float(input('Введите положительное число, которое хотите возвести в степень: '))
        if a != 0 and a > 0:
            break
    except ValueError:
        print('Ошибка формат ввода')
while True:
    try:
        b = int(input('Введите отрицательное число: '))
        if b < 0:
            break
    except ValueError:
        print('Ошибка формат ввода')
my_func(a, b)
