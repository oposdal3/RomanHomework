my_list = [9, 7, 5, 3, 3, 1]
while True:
    try:
        number = int(input('Введите новый элемент рейтинга: '))
        if number <= my_list[len(my_list) - 1]:
            my_list.append(number)
        else:
            for i in range(len(my_list)):
                if number > my_list[i]:
                    my_list.insert(i, number)
                    break
        print(my_list)
        break
    except ValueError:
        print('Ошибка формат ввода')
