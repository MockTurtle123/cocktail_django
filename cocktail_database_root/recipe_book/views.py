from django.shortcuts import render
from django.views import generic
from .forms import GetSelection
from .functions import *


class NameList(generic.ListView):
    queryset = Cocktail.objects.order_by('name').distinct()
    template_name = 'index.html'
    object_list = Cocktail.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        name_list = []
        ingredient_selected = self.request.session['ingredient_selected']
        if ingredient_selected:
            name_list.clear()
            for cocktail in Cocktail.objects.order_by().values():
                try:
                    for item in cocktail['ingredients']:
                        if item['ingredient'] == ingredient_selected:
                            name_list.append(cocktail['name'])
                except KeyError:
                    continue
            print(name_list)

        else:
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
            request.session['name_selected'] = form.cleaned_data['name']
            request.session['ingredient_selected'] = form.cleaned_data['ingredient']

        request.session['recipe'] = return_recipe(name=request.session['name_selected'])

        context = self.get_context_data()
        return render(request,'index.html', context=context)


def update(request):
    update_cocktail_data()
    return render(request, 'update.html')
