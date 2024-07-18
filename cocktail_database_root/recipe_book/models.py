from django.db import models



class Cocktail(models.Model):
    name = models.CharField(max_length=50)
    glass = models.CharField(max_length=10)
    garnish = models.CharField(max_length=100)
    ingredients = models.JSONField()
    preparation = models.CharField(max_length=500, default='')

    objects = models.Manager()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


