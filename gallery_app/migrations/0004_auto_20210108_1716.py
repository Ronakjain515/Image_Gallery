# Generated by Django 3.1.5 on 2021-01-08 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery_app', '0003_imagepost_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='rotateAngle',
        ),
        migrations.RemoveField(
            model_name='images',
            name='rotateAngle',
        ),
    ]
