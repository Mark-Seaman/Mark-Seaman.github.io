from django.urls import path

from notes.views import IndexPage, NoteCreate, NoteDetail, NoteList, NoteUpdate


urlpatterns = [

    # Notes
    path('', NoteList.as_view(), name='note-list'),
    path('<int:pk>', NoteDetail.as_view(), name='note-detail'),
    path('add', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/', NoteUpdate.as_view(), name='note-edit'),

]
