"""
Модуль для работы с рецептами. Содержит класс Recipe
"""

from typing import List, Dict
from .ingredient import Ingredient


class Recipe:
    """Класс для представления кулинарного рецепта."""

    def __init__(self, name: str, ingredients: List[Ingredient] = None,
                 description: str = "", instructions: str = "", category: str = "Основное"):
        """
        Инициализирует рецепт.
        
        """
        self._name = name
        self._ingredients = ingredients if ingredients is not None else []
        self._description = description
        self._instructions = instructions
        self._category = category

    @property
    def name(self) -> str:
        """
        
        :return: 
        """
        return self._name

    @name.setter
    def name(self, value: str):
        """
            
        :param value: 
        :return: 
        """
        if not value or not value.strip():
            raise ValueError("Название рецепта не может быть пустым")
        self._name = value.strip()

    @property
    def ingredients(self) -> List[Ingredient]:
        """
        
        :return: 
        """
        return self._ingredients

    @property
    def description(self) -> str:
        """
        
        :return: 
        """
        return self._description

    @description.setter
    def description(self, value: str):
        """
        
        :param value: 
        :return: 
        """
        self._description = value

    @property
    def instructions(self) -> str:
        """
        
        :return: 
        """
        return self._instructions

    @instructions.setter
    def instructions(self, value: str):
        """
        
        :param value: 
        :return: 
        """
        self._instructions = value

    @property
    def category(self) -> str:
        """
        
        :return: 
        """
        return self._category

    @category.setter
    def category(self, value: str):
        """
        
        :param value: 
        :return: 
        """
        self._category = value

    def add_ingredient(self, ingredient: Ingredient):
        """
        
        :param ingredient: 
        :return: 
        """
        self._ingredients.append(ingredient)

    def remove_ingredient(self, ingredient_name: str) -> bool:
        """
        
        :param ingredient_name: 
        :return: 
        """
        for i, ingredient in enumerate(self._ingredients):
            if ingredient.name.lower() == ingredient_name.lower():
                del self._ingredients[i]
                return True
        return False

    def calculate_calories(self) -> float:
        """
        
        :return: 
        """
        return sum(ingredient.total_calories() for ingredient in self._ingredients)

    def get_ingredient_names(self) -> List[str]:
        """
        
        :return: 
        """
        return [ingredient.name for ingredient in self._ingredients]

    def contains_ingredient(self, ingredient_name: str) -> bool:
        """
        
        :param ingredient_name: 
        :return: 
        """
        return any(ingredient.name.lower() == ingredient_name.lower()
                   for ingredient in self._ingredients)

    def str(self) -> str:
        """
        
        :return: 
        """
        ingredients_str = "\n".join(f"  - {ingredient}" for ingredient in self._ingredients)
        return (f"Рецепт: {self._name}\n"
                f"Категория: {self._category}\n"
                f"Описание: {self._description}\n"
                f"Ингредиенты:\n{ingredients_str}\n"
                f"Калории: {self.calculate_calories():.1f}")

    def repr(self) -> str:
        """
        
        :return: 
        """
        return f"Recipe(name='{self._name}', ingredients={len(self._ingredients)})"

    def to_dict(self) -> dict:
        """
        
        :return: 
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
        """
        
        :param data: 
        :return: 
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

