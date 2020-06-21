
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from mainApp.models import SERVICES, About, Portfolio, Team
from .views import IndexView


urlpatterns = [
    path('', 
    IndexView.as_view(),
    name="home_list"
        ),
]