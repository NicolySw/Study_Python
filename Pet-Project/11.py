class Car:

    def __init__(self, model, owner, mileage, color, engine_power):
        self.model = model
        self.owner = owner
        self.mileage = mileage
        self.engine_power = engine_power
        self.color = color

    def drive(self, distance):
        self.mileage += distance
        print(f'Модель {self.model} имеет пробег: {self.mileage}')


class Toyota(Car):

    def get_model(self):
        return f"Model: {self.model}"

    def get_horsepower(self):
        return f"Engine power: {self.engine_power}"

    def drive(self, distance):
        super().drive(distance)


class Renault(Car):
    pass


Car1 = Toyota('Camry', "Петя", 1000, "Red", 115)

Car2 = Toyota('Camry', "Вася", 1000, "Black", 115)
Car1.drive(1000)
Car1.drive(2000)
Car2.drive(1000)

print(Car1.owner)
print(dir(Car1))

