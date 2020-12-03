from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    
class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.pk
        return super().form_valid(form)
    

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = '__all__'
    

class BlogDeleteView(LoginRequiredMixin, DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
