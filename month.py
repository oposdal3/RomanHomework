mymonthlist = ['Зима', 'Весна', 'Лето', 'Осень']
mymonthdict = {12: 0, 1: 0, 2: 0, 3: 1, 4: 1, 5: 1, 6: 2, 7: 2, 8: 2, 9: 3, 10: 3, 11: 3}
norm = False
while True:
    try:
        number = int(input('Введите число от 1 до 12 включительно: '))
        print(mymonthlist[mymonthdict[number]])
        break
    except ValueError:
        print('Ошибка формат ввода')
