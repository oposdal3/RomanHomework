class Error(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


class Stock:
    storage = {1: {'Имя': 'Кранштат', 'Цена': 25000, 'Колличество': 7}}

    def __init__(self, j, name, price, kol):
        self.storage[j] = {'Имя': name, 'Цена': price, 'Колличество': kol}

    def __str__(self):
        return f'{self.storage}'


class OfficeEquipment:
    def __init__(self, name, price, kol):
        self.name = name
        self.price = int(price)
        self.kol = int(kol)

    def __str__(self):
        return f'У {self.name} цена за 1 товар {self.price}. Его количество {self.kol} штук.'

    def keeping(self, pol):
        return Stock(pol, self.name, self.price, self.kol)


class Printer(OfficeEquipment):
    def __init__(self, name, price, kol):
        super().__init__(name, price, kol)


class Scanner(OfficeEquipment):
    def __init__(self, name, price, kol):
        super().__init__(name, price, kol)


class Xerox(OfficeEquipment):
    def __init__(self, name, price, kol):
        super().__init__(name, price, kol)


i = 1
while True:
    print('Что вы хотите добавить (принтер, сканер или ксерокс)')
    print('Для проверки напишите склад')
    print('Если хотите прекратить ввод данных напишите stop')
    command = input('--->').lower()

    if command == 'принтер':
        a = input('Введите имя принтера -->')
        while True:
            try:
                b = input('Его цену за 1 тавар -->')
                number = input('Колличество тавара -->')
                if not b.isdigit() or not number.isdigit():
                    raise Error('Введите пожалуйста цену и количество в цифррах')
            except Error as err:
                print(err)
            else:
                break
        printer = Printer(a, b, number)
        print(printer)
        print('Хотите ли вы добавить его в склад (да, нет)')
        command = input('--->')
        while True:
            if command == 'да':
                printer.keeping(i)
                i += 1
                print(Stock.storage)
                break
            elif command == 'нет':
                break
            else:
                print('Пожалуйста введите внятную команду!!')
    elif command == 'сканер':
        a = input('Введите имя сканера -->')
        while True:
            try:
                b = input('Его цену за 1 тавар -->')
                number = input('Колличество тавара -->')
                if not b.isdigit() or not number.isdigit():
                    raise Error('Введите пожалуйста цену и количество в цифррах')
            except Error as err:
                print(err)
            else:
                break
        scanner = Scanner(a, b, number)
        print(scanner)
        print('Хотите ли вы добавить его в склад (да, нет)')
        command = input('--->')
        while True:
            if command == 'да':
                scanner.keeping(i)
                i += 1
                print(Stock.storage)
                break
            elif command == 'нет':
                break
            else:
                print('Пожалуйста введите внятную команду!!')
    elif command == 'ксерокс':
        a = input('Введите имя ксерокса -->')
        while True:
            try:
                b = input('Его цену за 1 тавар -->')
                number = input('Колличество тавара -->')
                if not b.isdigit() or not number.isdigit():
                    raise Error('Введите пожалуйста цену и количество в цифррах')
            except Error as err:
                print(err)
            else:
                break
        xerox = Xerox(a, b, number)
        print(xerox)
        print('Хотите ли вы добавить его в склад (да, нет)')
        command = input('--->')
        while True:
            if command == 'да':
                xerox.keeping(i)
                i += 1
                print(Stock.storage)
                break
            elif command == 'нет':
                break
            else:
                print('Пожалуйста введите внятную команду!!')
    elif command == 'stop':
        print('Программа остановленна!!')
        print(Stock.storage)
        break
    elif command == 'склад':
        print(Stock.storage)
    else:
        print('Пожалуйста введите внятную команду!!')
