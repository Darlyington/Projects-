# Generated by Django 5.1.2 on 2025-03-19 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DHIN_REVAMP', '0003_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
