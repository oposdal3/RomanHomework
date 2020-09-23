with open('text_3.txt', 'r', encoding='utf-8') as file:
    info = {}
    my_list = []
    sum_ = 0
    kol = 0
    for line in file:
        line = line.split()
        info[line[0]] = line[1].replace('\n', '')
    for el in info:
        if float(info[el]) < 20000:
            print(f'{el} имеет меньше 20000')
        kol += 1
        sum_ += float(info[el])
    print(f'Средняя окладка = {round(sum_ / kol, 1)}')

