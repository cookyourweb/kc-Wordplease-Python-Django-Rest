from django.contrib import admin
from articles.models import Category, Articulo

# Register your models here.
admin.site.register(Category),
admin.site.register(Articulo)