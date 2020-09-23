import json
with open('text_7.txt', 'r', encoding='utf-8') as file:
    list_ = []
    kol = 0
    average_profit = 0
    info = {}
    for line in file:
        line = line.split()
        sum_ = int(line[2]) - int(line[3])
        if sum_ > 0:
            average_profit += sum_
            kol += 1
        info[str(line[0])] = sum_
    list_.append(info)
    info = {'average_profit': average_profit / kol}
    list_.append(info)
with open('text_77.json', 'w', encoding='utf-8') as write_f:
    json.dump(list_, write_f, indent=4, ensure_ascii=False)
