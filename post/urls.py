from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('blog/', views.BlogView.as_view(), name="blog_list"),
    path('post_view/<int:pk>/', views.PostView.as_view(), name="single_post"),
    path('search/result/', views.searchResult, name="search")
]
