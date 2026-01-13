#!/usr/bin/python3

from setuptools import setup, find_packages

setup(
    name='recipebook', # Название вашей программы
    version='0.0.1', # Версия вашей программы.
    packages=find_packages("."),
    scripts=["bin/recipebook_main.py"], # Расположение главного исполняемого файла.
    url='https://github.com/zena876/RecipeBook.git', # Адрес репозитория с вашей курсовой работой.
    license='Apache-2.0',
    author='Наторова Евгения Михайловна', # ФИО автора.
    author_email='nzena605@gmail.com', # Электронная почта автора.
    description='Пакет для Python для работы с рецептами.'
                'Функционал:'
                'Добавить/удалить ингредиент,'
                'Добавить рецепт,'
                'Подсчитать калории,'
                'Сформировать список покупок,'
                'Найти рецепты по ингредиентам. ', # Описание вашей поделки. Что она может, для чего сделана.
    include_package_data=True,
    install_requires=[
      # Список зависимостей если есть.
      ],

)



