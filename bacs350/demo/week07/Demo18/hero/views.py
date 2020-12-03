from django.views.generic import TemplateView
from .models import Superhero


class HeroView(TemplateView):
    template_name="hero.html"
    
    def get_context_data(self, **kwargs):
        heroes = Superhero.objects.all()
        return {
            'title': 'Superhero Profile',
            'heroes': heroes,
        }