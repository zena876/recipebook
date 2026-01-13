"""
Модуль для работы с кулинарной книгой. Содержит класс Cookbook
"""

from typing import List, Dict, Optional
from .recipe import Recipe
from .ingredient import Ingredient


class Cookbook:
    """Класс для управления кулинарной книгой."""

    def __init__(self, filename: str = "cookbook.json"):
        """Инициализирует кулинарную книгу.
        """
        self._recipes: List[Recipe] = []

    @property
    def recipes(self) -> List[Recipe]:
        """Возвращает список рецептов.

        return список рецептов
        """
        return self._recipes

    @property
    def count(self) -> int:
        """Возвращает количество рецептов.

        return количество рецептов
        """
        return len(self._recipes)

    def add_recipe(self, recipe: Recipe) -> bool:
        """Добавляет рецепт в кулинарную книгу.
        """
        if any(r.name.lower() == recipe.name.lower() for r in self._recipes):
            return False

        self._recipes.append(recipe)
        return True

    def remove_recipe(self, recipe_name: str) -> bool:
        """Удаляет рецепт по названию.
        """
        for i, recipe in enumerate(self._recipes):
            if recipe.name.lower() == recipe_name.lower():
                del self._recipes[i]
                return True
        return False

    def get_recipe(self, recipe_name: str) -> Optional[Recipe]:
        """Находит рецепт по названию.

        return рецепт
        """
        for recipe in self._recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None

    def find_recipes_by_ingredient(self, ingredient_name: str) -> List[Recipe]:
        """Находит рецепты, содержащие указанный ингредиент.

        return рецепт с ингридиенотом
        """
        return [recipe for recipe in self._recipes
                if recipe.contains_ingredient(ingredient_name)]

    def find_recipes_by_category(self, category: str) -> List[Recipe]:
        """Находит рецепты по категории.

        return рецепт по категории
        """
        return [recipe for recipe in self._recipes
                if recipe.category.lower() == category.lower()]

    def generate_shopping_list(self, recipe_names: List[str]) -> Dict[str, float]:
        """Генерирует список покупок для указанных рецептов.
        """
        shopping_list = {}

        for recipe_name in recipe_names:
            recipe = self.get_recipe(recipe_name)
            if recipe:
                for ingredient in recipe.ingredients:
                    if ingredient.name in shopping_list:
                        shopping_list[ingredient.name] += ingredient.quantity
                    else:
                        shopping_list[ingredient.name] = ingredient.quantity

        return shopping_list

    def calculate_total_calories(self, recipe_names: List[str]) -> float:
        """Вычисляет общую калорийность для указанных рецептов.
                               """
        total = 0.0
        for recipe_name in recipe_names:
            recipe = self.get_recipe(recipe_name)
            if recipe:
                total += recipe.calculate_calories()
        return total

    def get_all_categories(self) -> List[str]:
        """Возвращает список всех категорий рецептов."""
        categories = set()
        for recipe in self._recipes:
            categories.add(recipe.category)
        return list(categories)

    def __str__(self) -> str:
        """Строковое представление кулинарной книги."""
        if not self._recipes:
            return "Кулинарная книга пуста"

        result = f"Кулинарная книга ({self.count} рецептов):\n"
        for recipe in self._recipes:
            result += f"\n- {recipe.name} ({recipe.category})"
        return result

    def print_shopping_list(self, recipe_names: List[str]):
        """Печатает список покупок для указанных рецептов."""
        shopping_list = self.generate_shopping_list(recipe_names)

        if not shopping_list:
            print("Список покупок пуст")
            return

        print("Список покупок:")
        for ingredient, quantity in shopping_list.items():
            print(f"{ingredient}: {quantity} г")



