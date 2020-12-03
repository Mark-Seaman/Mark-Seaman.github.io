from django.views.generic import TemplateView

from .workshop import accordion_data, card_data, cards_data, markdown_file_data, table_data, tabs_data


class HomeView(TemplateView):
    template_name = 'workshop.html'

    
class CardView(TemplateView):
    template_name = 'card.html'

    def get_context_data(self, **kwargs):
        return dict(card=card_data())


class CardsView(TemplateView):
    template_name = 'cards.html'

    def get_context_data(self, **kwargs):
        return dict(cards=cards_data())


class DocumentView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        doc = kwargs.get('doc', "README.md")
        return markdown_file_data(doc)
        
        
class TableView(TemplateView):
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        return dict(title='Lessons Schedule', 
                    table=table_data('Documents/lessons.csv'))
    
    
class TabsView(TemplateView):
    template_name = 'tabs.html'
    
    def get_context_data(self, **kwargs):
        tabs = tabs_data()
        return dict(title='Tab View', tabs=tabs)

    
class CarouselView(TemplateView):
    template_name = 'carousel.html'
    
    def get_context_data(self, **kwargs):
        carousel = carousel_data()
        return dict(title='Carousel View', carousel=carousel)
    

def carousel_data():
    return [["https://source.unsplash.com/random/1200x800?bear", "active"],
            ["https://source.unsplash.com/random/1200x800?forest", ''], 
            ["https://source.unsplash.com/random/1200x800?ocean"],
           ["https://source.unsplash.com/random/1200x800?flower"],
           ["https://images.unsplash.com/photo-1604932292784-ce6b48294afc"]]
    
class AccordionView(TemplateView):
    template_name = 'accordion.html'
    
    def get_context_data(self, **kwargs):
        return dict(accordion=accordion_data())