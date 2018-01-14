from django.contrib import admin

# Register your models here.
from django.contrib import admin

from articles.models import Category, Article

admin.site.register(Category)
admin.site.register(Article)