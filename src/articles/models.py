from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):  # 0 parametros
        """
        Devuelve la representación de un objeto como una string
        """
        return self.namegit



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

    def __str__(self):
        return self.title







