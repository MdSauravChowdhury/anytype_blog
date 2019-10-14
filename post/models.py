from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    image = models.ImageField(upload_to='author/picture/', blank=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title

class EmailSubcribe(models.Model):
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.email

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=150)
    thumbnail = models.ImageField(upload_to='post/images/')

    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    comment_count = models.PositiveIntegerField(default=150)
    view_count = models.PositiveIntegerField(default=150)

    category = models.ManyToManyField(Category)
    text = RichTextField()
    featured = models.BooleanField()


    # That is optional next post and previews post
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    previews_post = models.ForeignKey('self', related_name='previews', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:single_post", kwargs={"pk": self.pk})
    
