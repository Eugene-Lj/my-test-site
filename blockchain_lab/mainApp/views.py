from django.shortcuts import render
from django.views import generic
from .models import SERVICES, About, Portfolio, Team

class IndexView(generic.ListView):
    context_object_name = 'home_list'
    template_name = 'mainApp/posts.html'
    queryset = Portfolio.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['about_list'] = About.objects.all()
        context['team_list'] = Team.objects.all()
        context['services_list'] = SERVICES.objects.all()
        # And so on for more models
        return context


'''def index(request):
    return render(request, 'mainApp/index.html')

class PortfolioList(generic.ListView):
    model = Portfolio
    queryset = Portfolio.objects.all()
    template_name = 'mainApp/posts.html'

class AboutList(generic.ListView):
    model = About
    queryset = About.objects.all()
    template_name = 'mainApp/about_list.html' '''
