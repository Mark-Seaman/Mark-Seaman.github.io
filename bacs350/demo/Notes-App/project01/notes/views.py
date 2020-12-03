from django.http import HttpResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. This is a simple HTML page.")


class HomePageView(TemplateView):
    template_name = 'index.html'

