import inspect
from pprint import pprint


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


def introspection_info(obj):
    info = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}

    for name in dir(obj):
        if callable(getattr(obj, name)):
            info['methods'].append(name)
        else:
            info['attributes'].append(name)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info['module'] = __name__
    else:
        info['module'] = obj_module.__name__

    return info


if __name__ == '__main__':

    Car1 = Toyota('Camry', "Петя", 1000, "Red", 115)
    obj_ = Car1
    number_info = introspection_info(obj_)
    pprint(number_info)
