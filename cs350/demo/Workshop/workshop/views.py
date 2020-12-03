from django.views.generic import TemplateView

from .workshop import accordion_data, card_data, cards_data, markdown_file_data, super_data, table_data, tabs_data
from .menu import load_menu, load_side_menu


class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'super.html'

    def get_context_data(self, **kwargs):
        return dict(card=card_data(),menu = load_menu('README.md'))


class CardsView(TemplateView):
    template_name = 'super.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data(), menu = load_menu('README.md'))


class DocumentView(TemplateView):
    template_name = 'super.html'

    def get_context_data(self, **kwargs):
        menu = load_menu('README.md')
#        sidemenu = load_side_menu('README.md')
        doc = kwargs.get('doc', "README.md")
        return dict(card=markdown_file_data(doc), menu=menu)
#    , sidemenu=sidemenu)
        
        
class TableView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Lessons Schedule', 
                    table=table_data('Documents/lessons.csv'),
                   menu = load_menu('README.md'))
    
    
class TabsView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs, menu = load_menu('README.md'))

    
class CarouselView(TemplateView):
    template_name = 'carousel.html'
    
    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel, menu = load_menu('README.md'))
    

    
class SuperView(TemplateView):
    template_name = 'super.html'
    
    def get_context_data(self, **kwargs):
        return super_data()

    
class AccordionView(TemplateView):
    template_name = 'accordion.html'
    
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())