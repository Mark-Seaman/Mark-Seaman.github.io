from django.urls import path

from .views import (
    HeroListView,
    HeroDetailView,
    HeroCreateView,
    HeroUpdateView,
    HeroDeleteView,
)

urlpatterns = [
    path('hero/<int:pk>/delete/', HeroDeleteView.as_view(), name='hero_delete'),
    path('hero/new/', HeroCreateView.as_view(), name='hero_new'),
    path('hero/<int:pk>/', HeroDetailView.as_view(), name='hero_detail'),
    path('hero/<int:pk>/edit/', HeroUpdateView.as_view(), name='hero_edit'),
    path('hero/', HeroListView.as_view(), name='hero_list'),
]
