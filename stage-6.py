def protect(s):
    lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    return lower.intersection(s.lower()) != set()


def my_func(text):
    return text.title()


while True:
    a = input('Введите строку : ').split()
    for el in a:
        if protect(el):
            print('Неправильна была введена строка!!')
            break
    else:
        b = ''
        for el in a:
            b += el + ' '
        break
print(my_func(b))
