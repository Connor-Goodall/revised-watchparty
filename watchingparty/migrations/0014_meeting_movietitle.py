# Generated by Django 4.1.dev20220319144148 on 2022-04-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchingparty', '0013_meeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='movieTitle',
            field=models.CharField(default='', max_length=200),
        ),
    ]
