from django.urls import path, include

from .views import AboutView, BaseView


urlpatterns = [
    
    path('', BaseView.as_view(), name='base'),
    path('about', AboutView.as_view(), name='base'),
    
]
