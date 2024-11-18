"""
    Общее ТЗ:
    Реализовать классы Figure(родительский), Circle, Triangle и Cube,
    объекты которых будут обладать методами изменения размеров, цвета и т.д.
    Многие атрибуты и методы должны быть инкапсулированны и для них должны быть
    написаны интерфейсы взаимодействия (методы) - геттеры и сеттеры.
"""
import math


class Figure:
    sides_count = 0

    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = self.__is_filled()

    # Метод для получения цвета
    def get_color(self):
        return self.__color

    # Метод для проверки корректности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    # Метод для установки нового цвета
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = self.__is_filled()

    def __is_filled(self):
        # Проверяет, установлен ли цвет фигуры в значение, отличное от (0, 0, 0).
        return self.__color != [0, 0, 0]

    # Внутренний метод для проверки корректности сторон
    def __is_valid_sides(self, *sides):
        return all(isinstance(s, int) and s > 0 for s in sides) and len(sides) == self.sides_count

    # Метод для получения сторон
    def get_sides(self):
        # Метод get_sides возвращает значение атрибута __sides.
        return self.__sides

    # Метод для получения периметра (суммы сторон)
    def __len__(self):
        # Метод __len__ возвращает периметр фигуры.
        return sum(self.__sides)

    # Метод для установки новых сторон
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    # Атрибут класса Circle: sides_count = 1
    sides_count = 1  # Длина окружности.

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(1)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_radius(self):
        return self.__radius

    # Метод для вычисления площади круга: Площадь_круга = 3,14 * Радиус ^ 2
    def get_square(self):
        # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        return math.pi * (self.__radius ** 2)


# Класс Triangle, наследуемый от Figure
class Triangle(Figure):
    # Атрибут класса Triangle: sides_count = 3
    sides_count = 3

    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)
        # Если количество сторон не соответствует ожиданиям, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))
        self.__height = self.__calculate_height()

    # Метод для получения высоты треугольника
    def get_height(self):
        return self.__height

    def __calculate_height(self):
        # Стороны треугольника
        first, second, third = self.get_sides()
        half_of_per = sum([first, second, third]) / 2
        # Площадь треугольника
        area = math.sqrt(half_of_per * (half_of_per - first) * (half_of_per - second) * (half_of_per - third))
        return 2 * area / first

    # Метод для вычисления площади треугольника: Площадь_треугольника = 0,5 * Основание * Высота
    def get_square(self):
        # Метод get_square возвращает площадь треугольника.
        first, _, _ = self.get_sides()
        return 0.5 * first * self.__height


# Класс Cube, наследуемый от Figure
class Cube(Figure):
    # Атрибут класса Cube: sides_count = 12
    sides_count = 12

    def __init__(self, color=(0, 0, 0), *sides):
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)
        # Если количество сторон не соответствует ожиданиям, устанавливаем значение по умолчанию
        if len(self.get_sides()) != self.sides_count:
            self.set_sides(*([1] * self.sides_count))

    # Метод для вычисления объема куба
    def get_volume(self):
        side_length = self.get_sides()[0]
        # Метод get_volume, возвращает объём куба.
        return side_length ** 3


# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
