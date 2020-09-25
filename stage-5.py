class Stationery:
    def __init__(self):
        self.title = 'Кратинка'
        self.draw()

    def draw(self):
        return f'Запуск отрисовки. {self.title} рисуется '


class Pen(Stationery):
    def control(self):
        print(f'{self.draw()}с помощью Ручки!')


class Pencil(Stationery):
    def control(self):
        print(f'{self.draw()}с помощью Карандаша!')


class Handle(Stationery):
    def control(self):
        print(f'{self.draw()}с помощью Маркер!')


write = Pen()
write.control()
write = Pencil()
write.control()
write = Handle()
write.control()
