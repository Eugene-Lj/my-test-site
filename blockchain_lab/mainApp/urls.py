
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from mainApp.models import SERVICES, About, Portfolio, Team
from .views import IndexView
#from django.views.generic import list_detail

urlpatterns = [
    #path('', views.index, name='index'),
    #path('post', ListView.as_view(queryset=Portfolio.objects.all(),
    #template_name="mainApp/posts.html")),
    #path('post', ListView.as_view(queryset=About.objects.all(),
    #template_name="mainApp/posts.html")),
    #path('post', views.PortfolioList.as_view()),
    #path('post', views.AboutList.as_view()),
    path('', 
    IndexView.as_view(),
    name="home_list"
        ),
]