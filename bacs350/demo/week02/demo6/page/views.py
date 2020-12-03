from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page', 
            'body': 'Once upon a time ...',
        }
    
    
class HeroView(TemplateView):
    template_name = "hero.html"
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'Once upon a time ...',
        }
    
    
class ProfileView(TemplateView):
    template_name = "page.html"
    
    def get_context_data(self, **kwargs):
        return {
            'title': 'My Profile Page', 
            'body': 'Once upon a time ...',
        }