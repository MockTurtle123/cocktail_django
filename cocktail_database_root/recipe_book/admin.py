from django.contrib import admin
from .models import Cocktail


class CocktailItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'glass')
    list_filter = ('name',)
    search_fields = ('name',)


# Register your models here.
admin.site.register(Cocktail, CocktailItemAdmin)