class NuclearReactor:
    """Базовый класс Ядерного реактора"""

    def __init__(self, capacity: float):
        """
        Создание и подготовка к работе объекта "Ядерный реактор"

        :param capacity: Мощность ядерного реактора в МВт
        """
        self.capacity = capacity

    def __str__(self):
        return f"Ядерный реактор мощностью {self.capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(capacity={self.capacity!r})"

    def regulation_of_reactivity(self, reactivity: float) -> float:
        """
        Регулирование реактивности реактора за счет глубины погружения органов Системы управления и защиты(СУЗ)
        :reactivity: Показывает реактивность реактора
        :return: Возвращает глубину, на которую нужно погрузить СУЗы для возвращения реактивности в 0
        """
        ...
        immersion_depth = ...
        return immersion_depth

    def reactor_start_up(self) -> None:
        """
        Данный метод отвечает за пуск реактора, который происходит за счет подъема из активной зоны
        нескольких кластеров органов СУЗ
        """
        ...


class PressurizedWaterReactor(NuclearReactor):
    """Дочерний класс Ядерного реактора с водой под давлением"""

    def __init__(self, capacity: float, pressure_1: float):
        """
        Создание и подготовка к работе объекта "Ядерный реактор с водой под давлением"

        :capacity: Мощность реактора, наследуем из базового класса
        :param pressure_1: Давление 1 контура в МПа
        """
        super().__init__(capacity)
        self.pressure_1 = pressure_1

    def __str__(self):
        return f"Ядерный реактор с водой под давлением {self.pressure_1} и мощностью {self.capacity}"

    def __repr__(self):
        return f"{self.__class__.__name__}(capacity={self.capacity!r}, pressure_1={self.pressure_1})"

    def regulation_of_reactivity(self, reactivity: float) -> str:
        """
        Регулирование реактивности реактора за счет глубины погружения органов Системы управления и защиты(СУЗ)
        и концентрации борной кислоты.
        Данный метод необходимо перегрузить, так как в реакторах с водой под давлением компенсация реактивности
        происходит не только за счет органов СУЗ, но и за счет введения в воду борной кислоты

        :reactivity: Показывает реактивность реактора
        :return: Возвращает глубину, на которую нужно погрузить СУЗы, а также концентрацию борной кислоты
         для компенсации реактивности
        """
        ...
        immersion_depth = ...
        concentration_of_boric_acid = ...
        return f"Глубина СУЗ = {immersion_depth}, Концентрация борной кислоты = {concentration_of_boric_acid}"
