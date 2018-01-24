from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):
        """
        :return: La representación de un objeto como un string
        """
        return self.name


class Blog(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='blog')
    blog_name = models.CharField(max_length=150)
    blog_description = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Blog.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.blog.save()


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=350)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    publish_date = models.DateField()
    categories = models.ManyToManyField(Category)
