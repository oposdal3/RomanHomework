number = int(input('Введите число: '))
more = 0
while number > 0:
    if number % 10 > more:
        more = number % 10
    number //= 10
print('Самое большое число:', more)
