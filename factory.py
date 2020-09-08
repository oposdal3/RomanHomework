moremoney = int(input('Введите выручку: '))
lowmoney = int(input('Введите издержек: '))
if moremoney > lowmoney:
    print('Ваша фирма приносит вам прибыль.')
    print('Ваша рентабельность выручки ', moremoney / lowmoney)
    people = int(input('Сколько сотрудников в вашей фирме?: '))
    print('Ваш расчёт прибыли на одного человека', moremoney / people)
else:
    print('Ваша фирма неcёт убытки.')
