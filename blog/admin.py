from django.contrib import admin
from .models import Post, Comment
from django_markdown.admin import MarkdownModelAdmin

admin.site.register(Post, MarkdownModelAdmin)
admin.site.register(Comment)