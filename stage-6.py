with open('text_6.txt', 'r', encoding='utf-8') as file:
    dict_ = {}
    for line in file:
        result = line.split()
        a = 0
        b = 0
        c = 0
        if result[1] != '-':
            a = int(result[1].replace('(л)', ''))
        if result[2] != '-':
            b = int(result[2].replace('(пр)', ''))
        if result[3] != '-':
            c = int(result[3].replace('(лаб)', ''))
        dict_[result[0].replace(':', '')] = a + b + c
    print(dict_)
