# Generated by Django 4.2.1 on 2023-05-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0027_music_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='is_like',
            field=models.BooleanField(default=False),
        ),
    ]
