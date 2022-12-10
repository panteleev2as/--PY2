from typing import Union
import doctest

# TODO Написать 3 класса с документацией и аннотацией типов
class NuclearReactor:
    def __init__(self, nominal_capacity: Union[int, float], nominal_pressure:  Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ядерный реактор ВВЭР"

        :param nominal_capacity: Номинальная мощность реактора, МВт
        :param nominal_pressure: Номинальное давление в реакторе, МПа

        Примеры:
        >>> Reactor = NuclearReactor(1000, 16)
        """
        if not nominal_capacity > 0:
            raise ValueError("Номинальная мощность должна быть положительной")
        if not isinstance(nominal_capacity, (int, float)):
            raise TypeError("Номинальная мощность должна быть числом")
        self.nominal_capacity = nominal_capacity

        if nominal_pressure < 0:
            raise ValueError("Давление не может быть отрицательным")
        if not isinstance(nominal_pressure, (int, float)):
            raise TypeError("Номинальное давление должно быть числом")
        self.nominal_pressure = nominal_pressure

    def is_reactor_under_control(self, current_capacity: Union[int, float]) -> bool:
        """
        Метод проверяет, находится ли реактор под контролем,
        сравнивая текущую и номинальную мощность

        :param current_capacity: Текущая мощность реактора, МВт
        :return: Под контролем ли реактор

        Примеры:
        >>> Reactor = NuclearReactor(1000, 16)
        >>> Reactor.is_reactor_under_control(800)
        True
        """
        if current_capacity < 0:
            raise ValueError("Текущая мощность не может быть отрицательной")
        if not isinstance(current_capacity, (int, float)):
            raise TypeError("Текущая мощность должна быть числом")
        return self.nominal_capacity >= current_capacity

    def is_boiling(self, current_temp: Union[int, float], current_pressure:  Union[int, float]) -> bool:
        """
        Метод проверяет на отсутствие объемного кипения в реакторе из условия, что температура насыщения
        при текущем давлении должна быть больше, чем текущая температура теплоносителя

        :param current_temp: Текущая температура теплоносителя, oC
        :param current_pressure: Текущее давление
        :return: Происходит ли объемное кипение

        Примеры:
        >>> Reactor = NuclearReactor(1000, 16)
        >>> Reactor.is_boiling(-278, 15)
        Traceback (most recent call last):
        ...
        ValueError: Температура не может быть ниже -273.15 градусов Цельсия
        """
        if current_temp < -273.15:
            raise ValueError("Температура не может быть ниже -273.15 градусов Цельсия")
        if not isinstance(current_temp, (int, float)):
            raise TypeError("Текущая температура должна быть числом")
        if current_pressure < 0:
            raise ValueError("Давление не может быть отрицательным")
        if not isinstance(current_pressure, (int, float)):
            raise TypeError("Текущее давление должно быть числом")
        ...


class Pen:
    def __init__(self, ink_volume: Union[int, float], length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ручка"

        :param ink_volume: Объем чернил, мл
        :param length: Длина ручки, см

        Примеры:
        >>> pen_1 = Pen(13, 15)
        """
        if ink_volume < 0:
            raise ValueError("Объем чернил не может быть отрицательным")
        if not isinstance(ink_volume, (int, float)):
            raise TypeError("Объем чернил должен быть числом")
        self.ink_volume = ink_volume

        if length < 0:
            raise ValueError("Длина ручки не может быть отрицательной")
        if not isinstance(length, (int, float)):
            raise TypeError("Длина должна быть числом")
        self.length = length

    def ink_replacement(self, new_ink_volume: Union[int, float]) -> Union[int, float]:
        """
        Метод производит замену стержня с чернилами в ручке

        :param new_ink_volume: Новое значение объема чернил

        Примеры:
        >>> pen_1 = Pen(13, 15)
        >>> pen_1.ink_replacement(15)
        15
        """
        if new_ink_volume < self.ink_volume:
            raise ValueError("Замена чернил не имеет смысла")
        if new_ink_volume < 0:
            raise ValueError("Объем чернил не может быть отрицательным")
        if not isinstance(new_ink_volume, (int, float)):
            raise TypeError("Объем чернил должен быть числом")

        self.ink_volume = new_ink_volume
        return self.ink_volume

    def is_pen_empty(self) -> bool:
        """
        Метод проверяет является ли ручка пустой
        :return: Является ли ручка пустой

        Примеры:
        >>> pen_1 = Pen(13, 15)
        >>> pen_1.is_pen_empty()
        False
        """
        return self.ink_volume == 0


class Computer:
    def __init__(self, turned_on: bool, memory_capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param turned_on: Состояние компьютера(включен(True), выключен(False))
        :param memory_capacity: Объем доступной памяти, Гб

        Примеры:
        >>> computer_1 = Computer(True, 512)
        """
        if not isinstance(turned_on, bool):
            raise TypeError("Компьютер должен быть либо включен(True), либо выключен(False)")
        self.turned_on = turned_on

        if not isinstance(memory_capacity, (int, float)):
            raise TypeError("Объем памяти должен быть числом в Гб")
        if not memory_capacity > 0:
            raise ValueError("Объем памяти компьютера должно быть положительным числом")
        self.memory_capacity = memory_capacity
        ...

    def switch(self) -> bool:
        """
        Метод включает или выключает компьютер в зависимости от текущего состояния
        Включает, если выключен и выключает, если включен

        :return: Состояние компьютера после выполнения метода

        Примеры:
        >>> computer_1 = Computer(True, 512)
        >>> computer_1.switch()
        False
        """
        self.turned_on = not self.turned_on
        return self.turned_on

    def downloading_program(self, program_size: Union[int, float]) -> Union[int,float]:
        """
        Метод загружает программу на компьютер, при этом уменьшается объем доступной памяти

        :param program_size: Объем, который займет программа на компьютере
        :return: Оставшийся объем памяти

        Примеры:
        >>> computer_1 = Computer(True, 512)
        >>> computer_1.downloading_program(12)
        500
        """
        if not isinstance(program_size, (int, float)):
            raise TypeError("Объем программы должен быть числом в Гб")
        if not program_size > 0:
            raise ValueError("Объем программы должен быть положительным числом")
        if program_size > self.memory_capacity:
            raise ValueError("Программа не может быть загружена, недостаточно памяти")

        self.memory_capacity -= program_size
        return self.memory_capacity


if __name__ == "__main__":
    doctest.testmod()
