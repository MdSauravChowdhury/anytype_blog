from django.contrib import admin
from .models import (Author,
                    Category,
                    Post)
# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     # Select Query
#     list_display = ['__str__', 'title', 'category']
#     list_editable = ['title', 'category',]#'next_post', 'previews_post' 
#     class Meta():
#         model = Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)

