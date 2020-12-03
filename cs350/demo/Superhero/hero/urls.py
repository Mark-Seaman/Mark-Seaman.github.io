
from hero.views import HeroAddView, HeroDetailView, HeroEditView, HeroListView
from django.urls import path


urlpatterns = [
#    path('', HeroView.as_view()),
#    path('<str:identity>', HeroView.as_view()),
    path('', HeroListView.as_view(), name='hero_list'),
    path('<int:pk>', HeroDetailView.as_view(), name='hero_detail'),
    path('add', HeroAddView.as_view(), name='hero_add'),
    path('<int:pk>/', HeroEditView.as_view(), name='hero_edit'),
    
]

