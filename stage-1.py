with open('text_12.txt', 'a', encoding='utf-8') as file:
    print('Введите строку которую вы хотите ввести в файл')
    print('Пустая строка будет считаться окончанием ввода')
    while True:
        line = input('Запись в файл:')
        if line == '':
            with open('text_12.txt', 'r', encoding='utf-8') as read:
                print(read.read())
                break
        else:
            with open('text_12.txt', 'a', encoding='utf-8') as write:
                write.write(line + '\n')
            with open('text_12.txt', 'r', encoding='utf-8') as read:
                print(read.read())
