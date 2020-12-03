from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from os.path import exists

from .models import Superhero


#class HeroView(TemplateView):
#    template_name = "hero_detail.html"
#
#    def get_context_data(self, **kwargs):
#        hero = Superhero.objects.get(pk=1)
#        return {'hero': hero}


class HeroDetailView(DetailView):
    template_name = "hero_detail.html"
    model = Superhero
    
    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        image = kwargs['object'].image
        if not exists('static/' + image):
            kwargs['missing'] = True
        return kwargs
            
   

class HeroListView(ListView):
    template_name = "hero_list.html"
    model = Superhero
    
    
class HeroAddView(CreateView):
    template_name = "hero_edit.html"
    model = Superhero
    fields = '__all__'
    
    
class HeroEditView(UpdateView):
    template_name = "hero_add.html"
    model = Superhero
    fields = '__all__'
    
