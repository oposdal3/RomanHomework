print('Введите числа раазделённые пробелом.')
print('Программа будет выполняться до тех пор пока вы не укажите специальный символ (=)')
_sum = 0
end = False
warning = False
while not end:
    numbers = input().split()
    interval = 0
    for el in numbers:
        if el == '=':
            end = True
            break
        elif el.isdigit():
            interval += int(el)
            _sum += int(el)
        else:
            warning = True
            break
    if warning:
        warning = False
        print(f'Ошибка введения данных!!')
        print(f'Программа принимает только числа и символ через пробел!!')
        print(f'Если хотите выйти из программы используйте символ (=)')
    if not end:
        print(f'Сумма промежуточная состовляет = {interval}, Сумма общая = {_sum}')
    else:
        print(f'Сумма общая состовляет = {_sum}')
