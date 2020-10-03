class ComplexNumbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Первое число:{self.a} Второе число:{self.b}'

    def __add__(self, other):
        return f'Сумма равна {(self.a + other.a) + (self.b + other.b)}'

    def __mul__(self, other):
        return f'Произведение равно {(self.a * other.a - (self.b * other.b)) + (self.b * other.a)}'


compl_1 = ComplexNumbers(1, 2)
compl_2 = ComplexNumbers(2, -2)
print(compl_1)
print(compl_1 + compl_2)
print(compl_1 * compl_2)
