# Generated by Django 4.1.5 on 2023-01-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0005_alter_review_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.IntegerField(),
        ),
    ]
