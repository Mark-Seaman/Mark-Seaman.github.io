from .models import Superhero

def get_hero(hero_name):
    return Superhero.objects.get(name=hero_name)

