from django.urls import path

from views.views import BaseTemplatePage, CardView, HomePage, IndexPage, MarkdownView, PageView, StyledView


urlpatterns = [

    # Simple Class Views
    path('', IndexPage.as_view()),
    path('home', HomePage.as_view()),
    path('theme', BaseTemplatePage.as_view()),
    path('page', PageView.as_view()),
    path('styled', StyledView.as_view()),
    
    path('cards', CardView.as_view()),
    path('markdown', MarkdownView.as_view()),

]
