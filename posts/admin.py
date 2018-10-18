from django.contrib import admin
from .models import Post, Category, Labels


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'category', 'cover', 'comment']
    filter_horizontal = ('labels',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Labels)
