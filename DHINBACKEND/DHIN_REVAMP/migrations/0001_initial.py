# Generated by Django 5.1.2 on 2025-03-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_published', models.DateField()),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='newsletter_covers/')),
                ('num_subscribers', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_published'],
            },
        ),
    ]
