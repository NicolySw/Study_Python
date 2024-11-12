class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        # Атрибут owner(str) - владелец транспорта. (владелец может меняться)
        self.owner = owner
        # Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
        self.__model = model
        # Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__engine_power = engine_power
        # Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
        self.__color = color

    def get_model(self):
        """
            Возвращает строку: "Модель: <название модели транспорта>
        """
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        """
            Возвращает строку: "Мощность двигателя: <мощность>
        """
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        """Возвращает строку: "Цвет: <цвет транспорта>"""
        return f'Цвет: {self.__color}'

    def print_info(self):
        """
            Распечатывает результаты методов(в том же порядке): get_model, get_horsepower, get_color;
            а так же владельца в конце в формате  "Владелец: <имя>"
        """
        print(f' {self.get_model()} \n {self.get_horsepower()} \n {self.get_color()} \n Владелец: {self.owner}')

    def set_color(self, new_color):
        """
            Принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке
            __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>
        """
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'\n Нельзя сменить цвет на {new_color} \n')


class Sedan(Vehicle):
    # Атрибут __PASSENGERS_LIMIT = 5 (в седан может поместиться только 5 пассажиров)
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        super().__init__(owner, model, color, engine_power)


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
