# Generated by Django 4.1.3 on 2023-02-18 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backapp', '0006_contactdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('PDCTNAME', models.CharField(blank=True, max_length=50, null=True)),
                ('CATEGORY', models.CharField(blank=True, max_length=100, null=True)),
                ('PRIZE', models.IntegerField(blank=True, null=True)),
                ('QUANTITY', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
