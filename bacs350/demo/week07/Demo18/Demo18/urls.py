from django.urls import path
from hero.views import HeroView

urlpatterns = [
    path('', HeroView.as_view()),
]
