class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def __str__(self):
        return f'дата {Data.extracting(self.day_month_year)}'

    @classmethod
    def extracting(cls, day_month_year):
        date = []
        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def validation(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Всё хорошо'
                else:
                    return f'неправильный год'
            else:
                return f'неправильный месяц'
        else:
            return f'неправильный день'


today = Data('20 - 10 - 2017')
print(today)
print(Data.validation(10, 12, 2020))
print(today.extracting('26 - 6 - 2008'))
print(Data.validation(30, 12, 2019))
