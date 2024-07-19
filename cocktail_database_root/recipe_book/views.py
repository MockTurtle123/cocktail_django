from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .forms import GetSelection
from .functions import *


class NameList(generic.ListView):
    queryset = Cocktail.objects.order_by('name').distinct()
    template_name = 'index.html'
    object_list = Cocktail.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            ingredient_selected = self.request.session['ingredient_selected']
            name_list = Cocktail.objects.filter(ingredient__ingredient=ingredient_selected)
        except KeyError:
            name_list = Cocktail.objects.values_list('name', flat=True)

        ingredient_list = Ingredient.objects.filter(ingredient__isnull=False).values_list('ingredient', flat=True).distinct()

        context['ingredient_list'] = ingredient_list
        context['name_list'] = name_list

        return context

    def post(self, request):
        form = GetSelection(request.POST)
        if form.is_valid():
            request.session['name_selected'] = form.cleaned_data['name']
            request.session['ingredient_selected'] = form.cleaned_data['ingredient']

        else:
            messages.success(request, "Please select a name or an ingredient")

        if request.session['name_selected']:
            request.session['recipe'] = return_recipe(name=request.session['name_selected'])
            request.session.pop('ingredient_selected')

        context = self.get_context_data()
        return render(request, 'index.html', context=context)


def update(request):
    recipe_book_df = pd.read_json('recipes.json')
    for index, row in recipe_book_df.iterrows():
        c = Cocktail(
            name=row['name'],
            glass=row['glass'],
            garnish=row['garnish'],
            preparation=row['preparation'],
        )
        c.save()
        for item in row['ingredients']:
            i = Ingredient()
            try:
                i.amount = item['amount']
            except KeyError:
                pass

            try:
                i.ingredient = item['ingredient']
            except KeyError:
                pass

            try:
                i.label = item['label']
            except KeyError:
                pass

            try:
                i.special = item['special']
            except KeyError:
                pass

            i.cocktail = c
            i.save()
    return render(request, 'update.html')
