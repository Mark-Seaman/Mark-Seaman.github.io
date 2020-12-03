
from hero.views import AboutPage, BasePage, HeroView
from django.urls import path

urlpatterns = [
    path('', HeroView.as_view()),
    path('about', AboutPage.as_view()),
    path('base', BasePage.as_view()),
    path('<str:identity>', HeroView.as_view()),
]
