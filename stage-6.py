from itertools import count, cycle

print('Итератор count: ')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('Итератор cycle: ')
c = 0
for el in cycle('Москва'):
    if c > 11:
        break
    print(el, end='')
    c += 1
