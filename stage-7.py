def fact(number):
    verification = 1
    for i in range(1, number + 1):
        verification *= i
    yield verification


a = int(input('Введите число: '))
print([el for el in fact(a)])
