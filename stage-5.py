import random
with open('text_5.txt', 'w', encoding='utf-8') as file:
    kol = random.randint(1, 25)
    for i in range(kol):
        number = random.randint(1, 50)
        print(f'{number}', end=' ', file=file)
with open('text_5.txt', 'r', encoding='utf-8') as file:
    result = file.readline().split()
    sum_ = 0
    for el in result:
        sum_ += int(el)
    print(f'Сумма чисел в файле = {sum_}')
