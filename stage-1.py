from sys import argv

if len(argv) != 4:
    print('Количество параметров должн быть равен 4')
elif not argv[1].isdigit() and not argv[2].isdigit() and not argv[3].isdigit():
    print('В параметры необходимо ввести числа!!!')
else:
    name, output_in_hours, rate_per_hour, prize = argv


    def calculation(a, b, c):
        return float(a) * float(b) + float(c)


    print(calculation(output_in_hours, rate_per_hour, prize))
