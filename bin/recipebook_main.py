"""
Главный исполняемый модуль RecipeBook.
"""
from recipebook.cookbook import Cookbook
from recipebook.recipe import Recipe
from recipebook.ingredient import Ingredient

if __name__ == "__main__":
    """Основная функция - демонстрация работы пакета."""

    # Создаем кулинарную книгу
    cookbook = Cookbook()

    # Создаем ингредиенты
    eggs = Ingredient("Яйца", 3, "шт", 70)
    milk = Ingredient("Молоко", 100, "мл", 42)
    butter = Ingredient("Масло", 20, "г", 717)

    # Создаем рецепт омлета
    omelette = Recipe("Омлет классический", [eggs, milk, butter])

    # Добавляем рецепт в кулинарную книгу
    cookbook.add_recipe(omelette)

    # Выводим информацию
    print(f"1. Создан рецепт:{omelette}")

    print("\n2. Калорийность рецепта:,"
          f"   {omelette.calculate_calories():.1f} ккал")

    print("\n3. Рецепты в кулинарной книге:,"
          f"Всего рецептов: {cookbook.count}")

    # Демонстрация поиска
    print("\n4. Поиск рецептов с 'Яйца':")
    recipes = cookbook.find_recipes_by_ingredient("Яйца")
    for recipe in recipes:
        print(f"   - {recipe.name}")

    # Демонстрация списка покупок
    print("\n5. Список покупок для рецепта:")
    shopping_list = cookbook.generate_shopping_list(["Омлет классический"])
    for ingredient, quantity in shopping_list.items():
        print(f"   {ingredient}: {quantity} г")



