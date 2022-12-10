from typing import Union

# TODO Написать 3 класса с документацией и аннотацией типов
class NuclearReactor:
    def __init__(self, nominal_capacity: Union[int, float], nominal_pressure:  Union[int, float]):
        """
        Создание и подготовка к работе объекта "Ядерный реактор ВВЭР"

        :param nominal_capacity: Номинальная мощность реактора, МВт
        :param nominal_pressure: Номинальное давление в реакторе, МПа
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
        """
        if current_capacity < 0:
            raise ValueError("Текущая мощность не может быть отрицательной")
        if not isinstance(current_capacity, (int, float)):
            raise TypeError("Текущая мощность должна быть числом")
        ...

    def is_boiling(self, current_temp: Union[int, float], current_pressure:  Union[int, float]) -> bool:
        """
        Метод проверяет на отсутствие объемного кипения в реакторе из условия, что температура насыщения
        при текущем давлении должна быть больше, чем текущая температура теплоносителя

        :param current_temp: Текущая температура теплоносителя, oC
        :param current_pressure: Текущее давление
        :return: Происходит ли объемное кипение
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

        :param ink_volume: Объем чернил
        :param length: Длина ручки
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

    def ink_replacement(self, new_ink_volume: Union[int, float]):
        """
        Метод производит замену стержня с чернилами в ручке

        :param new_ink_volume: Новое значение объема чернил
        """
        if new_ink_volume < self.ink_volume:
            raise ValueError("Замена чернил не имеет смысла")
        if new_ink_volume < 0:
            raise ValueError("Объем чернил не может быть отрицательным")
        if not isinstance(new_ink_volume, (int, float)):
            raise TypeError("Объем чернил должен быть числом")
        ...

    def is_pen_empty(self) -> bool:
        """
        Метод проверяет является ли ручка пустой
        :return: Является ли ручка пустой
        """
        ...


class Computer:
    def __init__(self, turned_on: bool, memory_capacity: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Компьютер"

        :param turned_on: Состояние компьютера(включен(True), выключен(False))
        :param memory_capacity: Объем доступной памяти, Гб
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

    def switch(self):
        """
        Метод включает или выключает компьютер в зависимости от текущего состояния
        Включает, если выключен и выключает, если включен
        """
        ...

    def downloading_program(self, program_size: Union[int, float]) -> Union[int,float]:
        """
        Метод загружает программу на компьютер, при этом уменьшается объем доступной памяти

        :param program_size: Объем, который займет программа на компьютере
        :return: Оставшийся объем памяти
        """
        if not isinstance(program_size, (int, float)):
            raise TypeError("Объем программы должен быть числом в Гб")
        if not program_size > 0:
            raise ValueError("Объем программы должен быть положительным числом")
        if program_size > self.memory_capacity:
            raise ValueError("Программа не может быть загружена, недостаточно памяти")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
