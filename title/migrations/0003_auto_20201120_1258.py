# Generated by Django 3.0.5 on 2020-11-20 09:12
import csv
from itertools import islice

from django.contrib.auth import get_user_model
from django.db import migrations

from title.models import Comment

User = get_user_model()


def load_data(apps, schema_editor):
    Category = apps.get_model('title', 'Category')
    Genre = apps.get_model('title', 'Genre')
    Title = apps.get_model('title', 'Title')
    Review = apps.get_model('title', 'Review')
    Comments = apps.get_model('title', 'Comments')
    with open('data/category.csv', encoding='utf8') as f:
        """заполняем категории."""
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            obj, created = Category.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2],
            )

    with open('data/genre.csv', encoding='utf8') as f:
        """заполняем жанры"""
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            obj, created = Genre.objects.get_or_create(
                id=row[0],
                name=row[1],
                slug=row[2],
            )
    
    with open('data/titles.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            category = Category.objects.get(id=row[3])
            obj, created = Title.objects.get_or_create(
                id=row[0],
                name=row[1],
                year=row[2],
                category=category,
            )

    with open('data/genre_title.csv', encoding='utf8') as f:
        reader = csv.reader(f)
        for row in islice(reader, 1, None):
            title_id = row[1]
            genre_id = row[2]
            genres = Genre.objects.filter(id=genre_id)
            title = Title.objects.get(id=title_id)
            title.genre.set(genres)


class Migration(migrations.Migration):

    dependencies = [
        ('title', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_data),
    ]

