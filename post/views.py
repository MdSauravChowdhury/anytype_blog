from django.db.models import Count, Q
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView, DetailView

from .models import Post
from .models import Category
from .models import EmailSubcribe
from .forms import EmailNews

# Create your views here.

def get_category_count():
    queryset = Post.objects.values('category__title').annotate(Count('category__title'))
    return queryset

def searchResult(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)| 
            Q(text__icontains=query)
        )
    context = {
        'queryset':queryset
    }
    return render(request, 'blog/search_result.html', context)   


class IndexView(TemplateView):

    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['index_list_post'] = Post.objects.all()[:3]
        context['index_blog_post'] = Post.objects.all()[:3]

        return context

class BlogView(ListView):

    template_name = 'blog/blog.html'
    model = Post
    context_object_name = "post"
    ordering = '-timestamp'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        category_count = get_category_count() # CATEGORY COUNT
        
        context = super().get_context_data(**kwargs)
        context['category_count'] = category_count # CATEGORY COUNT
        context['category_item'] =  Category.objects.all() # show side tag category
        context["last_three_post"] = Post.objects.order_by('-id')[:3]
        return context
    

class PostView(DetailView):

    template_name = 'blog/post.html'
    model = Post
    context_object_name = "singel_blog"


    def get_context_data(self, **kwargs):
        category_count = get_category_count()
        context = super().get_context_data(**kwargs)
        context['category_count'] = category_count
        context['category_item'] =  Category.objects.all() # show side tag category
        context["last_three_post"] = Post.objects.order_by('-id')[:3]

        return context