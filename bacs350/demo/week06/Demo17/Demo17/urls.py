
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView


class HeroView(TemplateView):
    template_name="hero.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'Superheroes List',
            'name': 'Iron Man', 
            'identity': 'Tony Stark',
        }

urlpatterns = [
    path('', HeroView.as_view()),
]
