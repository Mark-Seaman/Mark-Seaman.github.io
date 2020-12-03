from django.conf.urls import url, include
from django.urls import path
from notes.views import IndexPage

urlpatterns = [

    # Default
    path('', root_view),

    # Index view
    path('index', IndexPage.as_view()),

    # Notes
    url(r'^note/', include('notes.urls')),
]
