from django.urls import path

from .views import AccordionView, CardView, CardsView, CarouselView, DocumentView, HomeView, SuperView, TableView, TabsView


urlpatterns = [
    
    path('',  HomeView.as_view(), name='workshop'),
    
    path('card',  CardView.as_view(), name='card'),
    path('cards',  CardsView.as_view(), name='cards'),
    
    path('doc/<str:doc>',  DocumentView.as_view(), name='doc'),
    
    path('table',  TableView.as_view(), name='table'),

    path('tabs',  TabsView.as_view(), name='tabs'),
    path('accordion',  AccordionView.as_view(), name='accordion'),
    path('carousel',  CarouselView.as_view(), name='carousel'),
    
    
    path('super',  SuperView.as_view(), name='super'),
    
]
