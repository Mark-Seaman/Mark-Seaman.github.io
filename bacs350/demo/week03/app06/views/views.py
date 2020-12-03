from django.template.loader import render_to_string
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from markdown import markdown


# -----------------------------------------
# Template Views

class BaseTemplatePage(TemplateView):
    template_name = 'page_theme.html'
    

class HomePage(TemplateView):
    template_name = 'home.html'


class IndexPage(TemplateView):
    template_name = 'index.html'


class PageView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        return dict(css='/static/views.css', title='My Page View')

    
class StyledView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return dict(css='/static/views.css', title='My Styled View', subtitle='Demonstrates View Inheritance')

    
# -----------------------------------------
# Markdown View

class MarkdownView(TemplateView):
    template_name = 'markdown.html'

    def get_context_data(self, **kwargs):
        html = markdown(open('README.md').read())
        return dict(css='/static/css/views.css', title='My Markdown View', html=html)

    
# -----------------------------------------
# Component Views

class CardView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        cards = {'cards': [
            dict(header='Mark', body='Mark Seaman', style='blue'),
            dict(header='Stacie', body='Stacie Seaman', style='green'),
            dict(header='Christine', body='Christine Lynn Seaman'),
        ]}
        cards = render_to_string('cards.html', cards)
        return dict(css='/static/views.css', title='My Card View', cards=cards)

