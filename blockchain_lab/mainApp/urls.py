
from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from mainApp.models import Posts

urlpatterns = [
    path('', views.index, name='index'),
    path('', ListView.as_view(queryset=Posts.objects.all().order_by("-date"),
    template_name="mainApp/posts.html")),
]