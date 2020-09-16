def division(number1, number2, place):

    print(round(number1 / number2, place))


while True:
    try:
        a = float(input('Введите первое число №1:'))
        break
    except ValueError:
        print('Ошибка формат ввода')
while True:
    try:
        b = float(input('Введите первое число №1:'))
        if b != 0:
            break
    except ValueError:
        print('Ошибка формат ввода')
while True:
    try:
        c = int(input('Введите первое число №1:'))
        break
    except ValueError:
        print('Ошибка формат ввода')
division(a, b, c)
