seconds = int(input('Введите секунды: '))
hours = seconds // 3600
seconds -= hours * 3600
minets = seconds // 60
seconds -= minets * 60
if hours < 10:
    hours = '0' + str(hours)
if minets < 10:
    minets = '0' + str(minets)
if seconds < 10:
    seconds = '0' + str(seconds)
print('Время ', hours, ':', minets, ':', seconds, sep='')
