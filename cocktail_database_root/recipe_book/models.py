from django.db import models


class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    glass = models.CharField(max_length=10)
    garnish = models.CharField(max_length=100)
    preparation = models.CharField(max_length=500, default='')

    objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    amount = models.IntegerField(null=True)
    ingredient = models.CharField(max_length=80, null=True)
    label = models.CharField(max_length=80, null=True)
    special = models.CharField(max_length=80, null=True)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.ingredient

    class Meta:
        ordering = ['ingredient']
