from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from catalog.models import Table

urlpatterns = [
    path('', ListView.as_view(queryset=Table.objects.all(),
    template_name="catalog/homePage.html")),
]