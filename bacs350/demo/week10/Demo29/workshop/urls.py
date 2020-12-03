from django.urls import path

from .views import CardView, CardsView, HomeView
#AccordionView,  ,, MarkdownView, SuperView, TabView


urlpatterns = [
    
    path('',  HomeView.as_view(), name='workshop'),
    
    path('card',  CardView.as_view(), name='card'),
    path('cards',  CardsView.as_view(), name='cards'),
    
    
#    path('accordion',  AccordionView.as_view(), name='accordion'),
#    path('tabs',  TabView.as_view(), name='tabs'),
#    path('markdown',  MarkdownView.as_view(), name='markdown'),
#    path('super',  SuperView.as_view(), name='super'),
    
]
