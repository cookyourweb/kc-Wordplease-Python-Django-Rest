from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):  # 0 parametros
        """
        Devuelve la representación de un objeto como una string
        """
        return self.name


class Article(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    summary = models.TextField()
    blog_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title