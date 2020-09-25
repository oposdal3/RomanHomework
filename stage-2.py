class Road:
    def __init__(self, length, width):
        try:
            self._length = length
            self._width = width
        except ValueError:
            print('Ошибка ввода данных')

    def kalkulation(self):
        length = self._length
        width = self._width
        mas = 25
        thickness = 5
        sum_ = length * width * mas * thickness
        return f'{length}м * {width}м * {mas}кг * {thickness}см = {int(sum_ / 1000)}т'


road = Road(20, 5000)
print(road.kalkulation())
