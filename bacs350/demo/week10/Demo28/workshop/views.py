from django.views.generic import TemplateView


class BaseView(TemplateView):
    template_name = 'theme.html'

class AboutView(TemplateView):
    template_name = 'about.html'
