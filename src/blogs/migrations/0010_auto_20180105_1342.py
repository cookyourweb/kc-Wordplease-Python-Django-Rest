# Generated by Django 2.0.1 on 2018-01-05 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20180105_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(),
        ),
    ]
