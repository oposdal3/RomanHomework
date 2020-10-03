class Error(Exception):
    def __init__(self, text_error):
        self.text_error = text_error


print('Вводите числа через enter')
print('Для остановки напишите stop')
list_ = []
while True:
    try:
        number = input('-->')
        if number == 'stop':
            break
        if not number.isdigit():
            raise Error('Вводите пожалуйста числа')
    except Error as err:
        print(err)
    else:
        list_.append(int(number))
print(list_)
