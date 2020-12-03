from django.shortcuts import render
from django.views.generic import ListView
from .models import Hero

class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'