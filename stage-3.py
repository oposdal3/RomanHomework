class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income["wage"] + self._income["bonus"]}'


work = Position('Павел', 'Крестов', 'Преподаааватель', 25000, 30000)
print(work.get_full_name())
print(work.get_total_income())
