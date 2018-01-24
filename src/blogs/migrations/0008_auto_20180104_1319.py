# Generated by Django 2.0.1 on 2018-01-04 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to=settings.AUTH_USER_MODEL),
        ),
    ]
