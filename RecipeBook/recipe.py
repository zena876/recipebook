"""
Модуль для работы с рецептами. Содержит класс Recipe
"""

from typing import List, Dict
from .ingredient import Ingredient


class Recipe:
    """Класс для представления кулинарного рецепта."""

    def __init__(self, name: str, ingredients: List[Ingredient] = None,
             description: str = "", instructions: str = "", category: str = "Основное"):
        """Инициализирует рецепт."""
        self._name = name
        self._ingredients = ingredients if ingredients is not None else []
        self._description = description
        self._instructions = instructions
        self._category = category

    @property
    def name(self) -> str:
        """Возвращает название рецепта.

        return Название рецепта
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """Устанавливает название рецепта.
        
        parm._name = название рецепта
        """
        if not value or not value.strip():
            raise ValueError("Название рецепта не может быть пустым")
        self._name = value.strip()

    @property
    def ingredients(self) -> List[Ingredient]:
        """Возвращает список ингредиентов.

        return список ингредиентов
        """
        return self._ingredients

    @property
    def description(self) -> str:
        """Возвращает описание рецепта.

        return описание рецепта
        """
        return self._description

    @description.setter
    def description(self, value: str):
        """Устанавливает описание рецепта.

        parm._description = описание рецепта
        """
        self._description = value

    @property
    def instructions(self) -> str:
        """Возвращает инструкции по приготовлению.

        return инструкции по приготовлению
        """
        return self._instructions

    @instructions.setter
    def instructions(self, value: str):
        """Устанавливает инструкции по приготовлению.
        
        parm._instructions = инструкции по приготовлению
        """
        self._instructions = value

    @property
    def category(self) -> str:
        """Возвращает категорию рецепта.
        
        return категория рецепта
        """
        return self._category

    @category.setter
    def category(self, value: str):
        """Устанавливает категорию рецепта.

        parm._category = категория рецепта
        """
        self._category = value

    def add_ingredient(self, ingredient: Ingredient):
        """Добавляет ингредиент в рецепт.
        
        param._ingredients.append(ингредиент)
        """
        self._ingredients.append(ingredient)

    def remove_ingredient(self, ingredient_name: str) -> bool:
        """Удаляет ингредиент из рецепта по названию."""
        for i, ingredient in enumerate(self._ingredients):
            if ingredient.name.lower() == ingredient_name.lower():
                del self._ingredients[i]
                return True
        return False

    def calculate_calories(self) -> float:
        """Вычисляет общую калорийность рецепта.

        return общая калорийность
        """
        return sum(ingredient.total_calories() for ingredient in self._ingredients)

    def get_ingredient_names(self) -> List[str]:
        """Возвращает список названий ингредиентов.
        
        return список названий ингредиентов
        """
        return [ingredient.name for ingredient in self._ingredients]

    def contains_ingredient(self, ingredient_name: str) -> bool:
        """Проверяет, содержит ли рецепт указанный ингредиент.
        
        return указанный ингредиент
        """
        return any(ingredient.name.lower() == ingredient_name.lower()
                   for ingredient in self._ingredients)

    def str(self) -> str:
        """Строковое представление рецепта.
        
        return рецепт
        """
        ingredients_str = "\n".join(f"  - {ingredient}" for ingredient in self._ingredients)
        return (f"Рецепт: {self._name}\n"
                f"Категория: {self._category}\n"
                f"Описание: {self._description}\n"
                f"Ингредиенты:\n{ingredients_str}\n"
                f"Калории: {self.calculate_calories():.1f}")

    def repr(self) -> str:
        """Представление рецепта для отладки.

        return рецепт
        """
        return f"Recipe(name='{self._name}', ingredients={len(self._ingredients)})"

    def to_dict(self) -> dict:
        """Преобразует рецепт в словарь.
        
        return словарь из рецепта
        """
        return {
            'name': self._name,
            'ingredients': [ingredient.to_dict() for ingredient in self._ingredients],
            'description': self._description,
            'instructions': self._instructions,
            'category': self._category
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Recipe':
        """Создает рецепт из словаря.

        return рецепт
        """
        recipe = cls(
            name=data['name'],
            description=data.get('description', ''),
            instructions=data.get('instructions', ''),
            category=data.get('category', 'Основное')
        )

        for ing_data in data['ingredients']:
            recipe.add_ingredient(Ingredient.from_dict(ing_data))


        return recipe


