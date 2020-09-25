class Car:
    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = int(speed)
            self.color = color
            self.name = name
            self.is_police = bool(is_police)
            self.show_speed()
        except ValueError:
            print("Не верно введены переменные")

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} останавилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        speed = self.speed
        return speed


class TownCar(Car):
    def control(self):
        if self.show_speed() > 60:
            print(f'{self.name} замеченно превышение скорости!!!!')
        else:
            print(f'Машина {self.name} соблюдает скоростной режим!')


class SportCar(Car):
    def control(self):
        print(f'Машина {self.name} может ехать больше 60 км/ч там, где это разрешенно!')


class WorkCar(Car):
    def control(self):
        if self.show_speed() > 40:
            print(f'{self.name} замеченно превышение скорости!!!!')
        else:
            print(f'Машина {self.name} соблюдает скоростной режим!')


class PoliceCar(Car):
    def control(self):
        if self.is_police:
            print(f'Машина {self.name} может превышать скоростной режим при включенных сигналах!!!')
            return self.is_police
        else:
            print(f'Машина {self.name} не является полицейской!!!')
            return self.is_police


car = TownCar(60, 'Красный', 'Lexus', False)
car.control()
car.go()
car.stop()
car.go()
car.turn('налево')
car = WorkCar(75, 'Белый', 'Жигули', False)
car.control()
car.go()
car.stop()
car.go()
car.turn('направо')
car = PoliceCar(75, 'Черно-белый', 'Ford', True)
car.control()
car.go()
car.stop()
car.go()
car.turn('направо')
car = SportCar(120, 'Фиолетовый', 'Hyundai', False)
car.control()
car.go()
car.stop()
car.go()
car.turn('направо')
