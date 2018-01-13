from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional


class Articulo(models.Model):



    title = models.CharField(max_length=150)
    summary = models.TextField()
    blog_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
