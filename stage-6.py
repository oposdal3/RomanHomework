def my_func(text):
    return text[0].title() + text[1:]


while True:
    a = input('Введите строку : ').split()
    for el in a:
        if not el.isalpha():
            print('Ошибка формат ввода данных')
            break
    else:
        b = ''
        for el in a:
            b += el + ' '
        break
print(my_func(b))
