class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f'Вместимость одного автобуса {self.name}: {capacity} пассажиров'


class Autobus(Transport):
    default_seating_capacity = 50

    def seating_capacity(self, capacity=default_seating_capacity):
        return super().seating_capacity(capacity)


autobus = Autobus('Renault Logan', 180, 12)

print(autobus.seating_capacity())
