from django.urls import path
from . import views

urlpatterns = [
    path('', views.NameList.as_view(), name='index'),
    path('update/', views.update_cocktail_data, name='update')
]
