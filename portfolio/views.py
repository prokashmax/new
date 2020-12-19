from django.shortcuts import render, get_object_or_404
from .models import project

# Create your views here.
def index(request):
    projects = project.objects.all()
    return render(request, 'index.html', {'projects' : projects})

# base page views

def base(request):
    return render(request, 'base.html')

def pot_view(request,pot_id):
    portfolioview = get_object_or_404(project,pk=pot_id)
    return render(request, 'portfolio_view.html',{'portfolioview':portfolioview})