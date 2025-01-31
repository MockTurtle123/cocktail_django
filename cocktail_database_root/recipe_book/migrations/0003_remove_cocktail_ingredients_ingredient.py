# Generated by Django 5.0.7 on 2024-07-23 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_book', '0002_alter_cocktail_options_cocktail_preparation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='ingredients',
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('ingredient', models.CharField(max_length=80)),
                ('label', models.CharField(max_length=80)),
                ('special', models.CharField(max_length=80)),
                ('cocktail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_book.cocktail')),
            ],
            options={
                'ordering': ['ingredient'],
            },
        ),
    ]
