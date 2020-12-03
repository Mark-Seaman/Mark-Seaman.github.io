from django.urls import path
from hero.views import HeroView

urlpatterns = [
    path('hero/<str:identity>', HeroView.as_view()),
]