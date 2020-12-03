from django.views.generic import TemplateView


class HulkView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {'title': 'hulk'}
    
class WidowView(TemplateView):
    template_name = "hero.html"
    
    def get_context_data(self, **kwargs):
        return {'title': 'black_widow'}