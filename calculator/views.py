from django.shortcuts import render

DATA = {
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
    # можете добавить свои рецепты ;)
}


def recipes(request, dishes=None):
    template_name = 'calculator/index.html'
    if dishes in DATA.keys():
        recipe = DATA[dishes]
        servings = int(request.GET.get('servings', 1))
        for k, v in recipe.items():
            recipe[k] = v*servings

        context = {
          'recipe': recipe
        }

        return render(request, template_name, context)
    elif dishes is None:
        template_name = 'calculator/recipes.html'
        option = []
        for i in DATA.keys():
            option.append(i)
        context = {
            'option': option
        }

        return render(request, template_name, context)

    else:
        template_name = 'calculator/index.html'
        return render(request, template_name)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
