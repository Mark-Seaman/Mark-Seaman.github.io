from django.conf.urls import url, include
from django.urls import path

from notes.views import IndexPage


urlpatterns = [
    
    # Index view
    path('', IndexPage.as_view()),
    
    # Notes
    url(r'^note/', include('notes.urls')),
]
    