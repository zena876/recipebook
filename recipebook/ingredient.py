
#Модуль для работы с ингредиентами.Содержит Ingredient


class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str = "г", calories_per_unit: float = 0.0):
        """
        Инициализирует ингредиент.
        :param name: имя
        :param quantity: количество
        :param unit: единица измерения
        :param calories_per_unit: калории
        """
        self._name = name
        self._quantity = quantity
        self._unit = unit
        self._calories_per_unit = calories_per_unit

    @property
    def name(self) -> str:
        """
        Возвращает название ингредиента.

        :return self._name: название ингредиента
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
        Устанавливает название ингредиента.


        :param value: название ингредиента
        """
        if not value or not value.strip():
            raise ValueError("Название ингредиента не может быть пустым")
        self._name = value.strip()

    @property
    def quantity(self) -> float:
        """
        Возвращает количество ингредиента.

        :return quantity: количество игредиента
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value: float):
        """
        Устанавливает количество ингредиента.


        :param value: количество игредиента
        """
        if value < 0:
            raise ValueError("Количество не может быть отрицательным")
        self._quantity = value

    @property
    def unit(self) -> str:
        """
        Возвращает единицу измерения.

        :return unit: единица измерения

        """
        return self._unit

    @unit.setter
    def unit(self, value: str):
        """Устанавливает единицу измерения.

        :param value: единица измерения
        """
        self._unit = value

    @property
    def calories_per_unit(self) -> float:
        """
        Возвращает калории на единицу измерения.
        :return calories_per_unit: калории
        """
        return self._calories_per_unit

    @calories_per_unit.setter
    def calories_per_unit(self, value: float):
        """
        Преобразует ингредиент в словарь.
        :param value: ингридиент
        :return: ингридиент
        """
        if value < 0:
            raise ValueError("Калории не могут быть отрицательными")
        self._calories_per_unit = value

    def total_calories(self) -> float:
        """
        стоковое представление ингредиента
        :return: ингредиент
        """
        return self._quantity * self._calories_per_unit

    def __str__(self) -> str:
        """
            представление ингредиента для отладки
        :return: ингредиент
        """
        return f"{self._name}: {self._quantity} {self._unit}"

    def __repr__(self) -> str:
        """ 
        строковое представление ингредиента
        :return: ингредиент
        """
        return f"Ingredient(name='{self._name}', quantity={self._quantity}, unit='{self._unit}')"

    def to_dict(self) -> dict:
        """
        Преобразует ингредиент в словарь.
        :return: ингредиент
        """
        return {
            'name': self._name,
            'quantity': self._quantity,
            'unit': self._unit,
            'calories_per_unit': self._calories_per_unit
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Ingredient':
        """
        Создает ингредиент из словаря.
        :param data: ингридиент
        """
        return cls(
            name=data['name'],
            quantity=data['quantity'],
            unit=data.get('unit', 'г'),
            calories_per_unit=data.get('calories_per_unit', 0.0)

        )





