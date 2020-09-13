mytradelist = []
print('Введите элементы.')
print('Каждый элемент вводится через enter')
print('Для окончания ввода оставте поле пустым и нажмите enter')
while True:
    Peremennay = input()
    if Peremennay == '':
        break
    else:
        mytradelist.append(Peremennay)
if len(mytradelist) % 2 == 0:
    for i in range(0, len(mytradelist) - 1, 2):
        mytradelist[i], mytradelist[i + 1] = mytradelist[i + 1], mytradelist[i]
else:
    for i in range(0, len(mytradelist) - 2, 2):
        mytradelist[i], mytradelist[i + 1] = mytradelist[i + 1], mytradelist[i]
print(mytradelist)