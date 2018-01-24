from django.contrib import admin
from blogs.models import Category, Post, Blog

admin.site.site_header = 'WordPlease Backoffice'
admin.site.site_title = 'WordPlease Backoffice'

admin.site.register(Category),


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ('blog_name', 'blog_description')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'image', 'intro', 'publish_date')
    list_filter = ('categories',)
    search_fields = ('title',)
    fieldsets = (
        ('General Data', {
            'fields': ('title', 'intro', 'body')
        }),
        ('Categories and Publish Date', {
            'fields': ('categories', 'publish_date')
        }),
        ('Additional Info', {
            'fields': ('user', 'image'),
        }),
    )
