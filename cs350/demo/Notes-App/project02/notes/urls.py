from django.urls import path

from notes.views import HomePage, IndexPage, NoteCreate, NoteDetail, NoteList, NoteUpdate, root_view


urlpatterns = [


    # Simple Class Views
    path('home', HomePage.as_view()),
    path('index', IndexPage.as_view()),

    # Notes
    path('', NoteList.as_view(), name='note-list'),
    path('<int:pk>', NoteDetail.as_view(), name='note-detail'),
    path('add', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/', NoteUpdate.as_view(), name='note-edit'),

]
