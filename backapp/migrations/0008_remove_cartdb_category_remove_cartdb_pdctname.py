# Generated by Django 4.1.3 on 2023-02-19 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0007_cartdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdb',
            name='CATEGORY',
        ),
        migrations.RemoveField(
            model_name='cartdb',
            name='PDCTNAME',
        ),
    ]
