from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from catalog.models import Procurement

urlpatterns = [
    path('', ListView.as_view(queryset=Procurement.objects.all(),
    template_name="catalog/homePage.html")),
]