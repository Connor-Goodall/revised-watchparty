# Generated by Django 4.1.dev20220319144148 on 2022-03-24 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchingparty', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favoriteMovies', models.CharField(max_length=200)),
                ('favoriteTVShows', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='DropDownModel',
        ),
    ]
