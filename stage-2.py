class Except(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


number1 = int(input('Введите число которое вы хотите разделить: '))
while True:
    try:
        number2 = int(input('Введите число на которрое вы хотите рразделить: '))
        if number2 == 0:
            raise Except('Нельзя делить на 0')
    except ValueError:
        print('Вы ввели не число')
    except Except as err:
        print(err)
    else:
        print(f'Ваш ответ {int(number1 / number2)}')
        break
