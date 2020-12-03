from django.conf.urls import url
from django.contrib.admin import site
from django.urls import path
from django.views.generic import FormView

from notes.views import IndexPage, NoteCreate, NoteForm, NoteDetail, NoteList, NoteUpdate


urlpatterns = [

    # Admin
    path(r'admin/', site.urls),

    # Notes
    path('', NoteList.as_view(), name='note-list'),
    path('<int:pk>', NoteDetail.as_view(), name='note-detail'),
    path('add', NoteCreate.as_view(), name='note-add'),
    path('<int:pk>/', NoteUpdate.as_view(), name='note-edit'),
    url(r'^note$', FormView.as_view(template_name="note_form.html",
                                    form_class=NoteForm)),

]
