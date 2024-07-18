from .models import Cocktail
import pandas as pd


def convert(cl: int | float) -> int:
    """convert cl to ml"""
    ml = cl * 10
    return int(ml)


def format_glass(name, glass):
    """prepare glass string"""
    article: str = "an" if glass.startswith("o") else "a"
    glass_str: str = f"{name} is typically served in {article} {glass} glass.\n\n"
    return glass_str


def format_ingredients(ingredients):
    ingredients_str: str = "Ingredients:\n"  # prepare ingredients for output
    for item in ingredients:
        try:
            ingredients_str += f"- {convert(item['amount'])}ml of {item['ingredient']} ({item['label']})\n"
        except KeyError:
            try:
                ingredients_str += f"- {convert(item['amount'])}ml of {item['ingredient']}\n"
            except KeyError:
                pass
        try:
            ingredients_str += f"- {item['special']}\n"
        except KeyError:
            pass
    return ingredients_str


def format_garnish(garnish):
    garnish_str: str = f"Usually garnished with {garnish.lower()}\n"
    return garnish_str

def return_recipe(name):
    name = name
    selection = Cocktail.objects.get(name=name)
    glass = selection.glass
    garnish = selection.garnish
    ingredients = selection.ingredients
    preparation = selection.preparation

    recipe: list = []

    recipe.append(format_glass(name, glass))
    recipe.append(format_ingredients(ingredients))

    if garnish != 'nan':
        recipe.append(format_garnish(garnish))

    recipe.append(f"Preparation: {preparation}")

    return recipe


def update_cocktail_data():
    """Load recipe data from json file"""
    recipe_book_df = pd.read_json('recipes.json')
    for index, row in recipe_book_df.iterrows():
        Cocktail.objects.create(
            name=row['name'],
            glass=row['glass'],
            garnish=row['garnish'],
            ingredients=row['ingredients'],
            preparation=row['preparation'],
        )