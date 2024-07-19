from .models import Cocktail, Ingredient
from django.core.exceptions import ObjectDoesNotExist
import pandas as pd


def convert(cl: int | float) -> int:
    """convert cl to ml"""
    ml = cl * 10
    return int(ml)


def format_glass(name: str, glass: str):
    """prepare glass string for output"""
    article: str = "an" if glass.startswith("o") else "a"
    glass_str: str = f"{name} is typically served in {article} {glass} glass."
    return glass_str


def format_ingredients(ingredients) -> list[str]:
    """prepare ingredients for output"""
    ingredients_output: list = ["<b>Ingredients:</b>"]  # prepare ingredients for output
    for item in ingredients:
        if item.label:
            ingredients_output.append(f"{convert(item.amount)}ml of {item.ingredient} ({item.label})")
        elif item.ingredient:
            ingredients_output.append(f"{convert(item.amount)}ml of {item.ingredient}")
        elif item.special:
            ingredients_output.append(f"{item.special}")
        else:
            continue

    return ingredients_output


def format_garnish(garnish: str) -> str:
    """prepare garnish string for output"""
    garnish_str: str = f"Usually garnished with {garnish.lower()}"
    return garnish_str


def return_recipe(name: str) -> list[str]:
    """output the full recipe"""
    name = name
    try:
        selection = Cocktail.objects.get(name=name)
    except ObjectDoesNotExist:
        selection = Cocktail.objects.get(name='Alexander')

    glass: str = selection.glass
    garnish: str = selection.garnish
    ingredients = selection.ingredient_set.all()
    preparation: str = selection.preparation

    recipe: list = []

    recipe.append(format_glass(name, glass))
    recipe.extend(format_ingredients(ingredients))

    if garnish != 'nan':
        recipe.append(format_garnish(garnish))

    recipe.extend(["<b>Preparation:</b>", preparation])

    return recipe
