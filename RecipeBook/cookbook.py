"""
Модуль для работы с кулинарной книгой. Содержит класс Cookbook
"""

import json
import os
from typing import List, Dict, Optional
from .recipe import Recipe
from .ingredient import Ingredient


class Cookbook:
    """Класс для управления кулинарной книгой."""

    def init(self, filename: str = "cookbook.json"):
        """Инициализирует кулинарную книгу.
        """
        self._recipes: List[Recipe] = []
        self._filename = filename
        self._load_from_file()

    @property
    def recipes(self) -> List[Recipe]:
        """Возвращает список рецептов."""
        return self._recipes

    @property
    def count(self) -> int:
        """Возвращает количество рецептов."""
        return len(self._recipes)

    def add_recipe(self, recipe: Recipe) -> bool:
        """Добавляет рецепт в кулинарную книгу.
        """
        if any(r.name.lower() == recipe.name.lower() for r in self._recipes):
            return False

        self._recipes.append(recipe)
        self._save_to_file()
        return True

    def remove_recipe(self, recipe_name: str) -> bool:
        """Удаляет рецепт по названию.
        """
        for i, recipe in enumerate(self._recipes):
            if recipe.name.lower() == recipe_name.lower():
                del self._recipes[i]
                self._save_to_file()
                return True
        return False

    def get_recipe(self, recipe_name: str) -> Optional[Recipe]:
        """Находит рецепт по названию.
        """
        for recipe in self._recipes:
            if recipe.name.lower() == recipe_name.lower():
                return recipe
        return None

    def find_recipes_by_ingredient(self, ingredient_name: str) -> List[Recipe]:
        """Находит рецепты, содержащие указанный ингредиент.
        """
        return [recipe for recipe in self._recipes
                if recipe.contains_ingredient(ingredient_name)]

    def find_recipes_by_category(self, category: str) -> List[Recipe]:
        """Находит рецепты по категории.
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

    def _save_to_file(self):
        """Сохраняет кулинарную книгу в файл."""
        try:
            data = {
                'recipes': [recipe.to_dict() for recipe in self._recipes]
            }
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")

    def _load_from_file(self):
        """Загружает кулинарную книгу из файла."""
        if os.path.exists(self._filename):
            try:
                with open(self._filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                self._recipes = []
                for recipe_data in data.get('recipes', []):
                    self._recipes.append(Recipe.from_dict(recipe_data))
            except Exception as e:
                print(f"Ошибка при загрузке файла: {e}")

    def str(self) -> str:
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
