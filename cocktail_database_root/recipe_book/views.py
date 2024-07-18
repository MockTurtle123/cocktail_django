from django.shortcuts import render
from django.views import generic
from .models import Cocktail
from .forms import GetSelection
import pandas as pd


class NameList(generic.ListView):
    queryset = Cocktail.objects.order_by('name').distinct()
    template_name = 'index.html'
    object_list = Cocktail.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name_list = []
        for item in Cocktail.objects.order_by().values('name'):
            if not item['name'] in name_list:
                name_list.append(item['name'])

        ingredient_list = []
        for item in Cocktail.objects.order_by().values('ingredients'):
            try:
                for ingredient in item['ingredients']:
                    if not ingredient['ingredient'] in ingredient_list:
                        ingredient_list.append(ingredient['ingredient'])
            except KeyError:
                continue
        context['ingredient_list'] = ingredient_list
        context['name_list'] = name_list

        return context

    def post(self, request):
        form = GetSelection(request.POST)
        if form.is_valid():
            request.session['name'] = form.cleaned_data['name']
            request.session['ingredient'] = form.cleaned_data['ingredient']

        context = self.get_context_data()
        return render(request,'index.html', context=context)



def update_cocktail_data(request):
    """Load recipe data from json file"""
    recipe_book_df = pd.read_json('recipes.json')
    for index, row in recipe_book_df.iterrows():
        Cocktail.objects.create(
            name=row['name'],
            glass=row['glass'],
            garnish=row['garnish'],
            ingredients=row['ingredients']
        )
    return render(request, 'update.html')


# def index(request):
#     cocktail_name = request.POST.get('choose_name', 'Alexander')
#
#     return render(request, 'index.html')