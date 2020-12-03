from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from notes.models import Note


# -----------------------------------------
# Custom Views

class IndexPage(TemplateView):
    template_name = 'index.html'


# -----------------------------------------
# Note Data Models

class NoteList(ListView):
    model = Note
    template_name = 'note_list.html'


class NoteDetail(DetailView):
    model = Note
    template_name = 'note_detail.html'


class NoteCreate(CreateView):
    model = Note
    fields = ['name']
    template_name = 'note_add.html'


class NoteUpdate(UpdateView):
    model = Note
    fields = ['name']
    template_name = 'note_edit.html'
