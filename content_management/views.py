from django.shortcuts import render,redirect
from django.views.generic import TemplateView, CreateView

from post.models import Post
# Create your views here.user_management

class UserPanel(TemplateView):
    template_name = "index.html"

        
class CreatePostView(CreateView):
    model = Post
    template_name = "form-advance.html"
    fields = ('__all__')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()

        return redirect('index')
        