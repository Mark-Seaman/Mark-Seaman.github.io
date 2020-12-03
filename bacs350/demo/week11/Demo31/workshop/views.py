from django.views.generic import TemplateView

from .workshop import card_data, cards_data, markdown_file_data, table_data


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
        doc = kwargs.get('doc', "REAsDME.md")
        return markdown_file_data(doc)
        
        
class TableView(TemplateView):
    template_name = 'table.html'
    
    def get_context_data(self, **kwargs):
        return dict(table=table_data('Documents/lessons.csv'))
    
    
