def my_func(number1, number2, number3):
    _sum1 = number1 + number2
    _sum2 = number2 + number3
    _sum3 = number3 + number1
    print(f'Большая сумма чисел: {max(_sum1, _sum2, _sum3)}')


while True:
    try:
        a = float(input('Введите первое число №1:'))
        break
    except ValueError:
        print('Ошибка формат ввода')
while True:
    try:
        b = float(input('Введите первое число №2:'))
        break
    except ValueError:
        print('Ошибка формат ввода')
while True:
    try:
        c = float(input('Введите первое число №3:'))
        break
    except ValueError:
        print('Ошибка формат ввода')
my_func(a, b, c)
