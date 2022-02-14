from django.shortcuts import render


def recipe(request, dish):
    data = {
        'omlet': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        },
        'pasta': {
            'макароны, г': 0.3,
            'сыр, г': 0.05,
        },
        'buter': {
            'хлеб, ломтик': 1,
            'колбаса, ломтик': 1,
            'сыр, ломтик': 1,
            'помидор, ломтик': 1,
        },
    }

    servings = int(request.GET.get("servings", 1))
    dish_recipe = data[f'{dish}']
    for ingredient, amount in dish_recipe.items():
        dish_recipe[ingredient] = amount * servings

    context = {
        'recipe': dish_recipe,
    }
    return render(request, 'calculator/index.html', context)

