# Generated by Django 4.2.1 on 2023-05-13 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0024_delete_spotify_playlist_music'),
    ]

    operations = [
        migrations.DeleteModel(
            name='spotify_playlist',
        ),
    ]
