# Generated by Django 4.0.3 on 2022-03-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchingparty', '0007_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='platform',
            field=models.CharField(default='movieStock.jpeg', max_length=200),
            preserve_default=False,
        ),
    ]
