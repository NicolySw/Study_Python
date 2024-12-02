class Car:
    def __init__(self, model: str, __vin: int, __number: str):
        self.model = model
        if self.__is_valid_vin(__vin):
            self.vin = __vin
        if self.__is_valid_number(__number):
            self.number = __number

    def __is_valid_vin(self, vin_number):
        """
            Проверка корректности Vin
        """
        if isinstance(vin_number, str):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif len(str(vin_number)) != 7:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        else:
            return True

    def __is_valid_number(self, number):
        """
            Проверка на корректность номера автомобиля
        """
        if not isinstance(number, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        elif len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')


try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
