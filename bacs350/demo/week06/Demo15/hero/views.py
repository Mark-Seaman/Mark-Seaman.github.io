from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy 

from .models import Hero


class HeroListView(ListView):
    model = Hero
    template_name = 'hero_list.html'


class HeroDetailView(DetailView):
    model = Hero
    template_name = 'hero_detail.html'


class HeroCreateView(CreateView):
    model = Hero
    template_name = 'hero_new.html'
    fields = ['title', 'author', 'body']


class HeroUpdateView(UpdateView):
    model = Hero
    template_name = 'hero_edit.html'
    fields = ['title', 'body']


class HeroDeleteView(DeleteView): # new
    model = Hero
    template_name = 'hero_delete.html'
    success_url = reverse_lazy('home')
