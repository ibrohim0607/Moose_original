from django.contrib import admin
from .models import Post, Comment, Contact, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Category)
