
from django.http import HttpResponse
from django.urls import path


def home_page_view(request):
    return HttpResponse("<p>"+"HOME"+"</p>")

def about_page_view(request):
    return HttpResponse("<h1>ABOUT</h1>")


urlpatterns = [
    path('home', home_page_view),
    path('about', about_page_view),
]
