from django.http import HttpResponse
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from notes.models import Note


# -----------------------------------------
# View Function

def root_view(request):
    html = "<h1>Hello, world.</h1>"
    html += "<p>This is a simple HTML page.</p>"
    html += '<p>Visit <a href="/views/">Default page</a>.</p>'
    html += '<p>Visit <a href="/views/home">Home page</a>.</p>'
    html += '<p>Visit <a href="/views/index">Index page</a>.</p>'
    return HttpResponse(html)


# -----------------------------------------
# Custom Views

class HomePage(TemplateView):
    template_name = 'home.html'


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
