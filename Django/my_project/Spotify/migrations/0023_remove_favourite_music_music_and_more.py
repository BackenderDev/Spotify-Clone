# Generated by Django 4.2.1 on 2023-05-13 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0022_rename_album_id_favourite_album_album_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite_music',
            name='music',
        ),
        migrations.RemoveField(
            model_name='favourite_music',
            name='user',
        ),
        migrations.RemoveField(
            model_name='playlist_music',
            name='music',
        ),
        migrations.RemoveField(
            model_name='playlist_music',
            name='playlist',
        ),
        migrations.DeleteModel(
            name='Favourite_Album',
        ),
        migrations.DeleteModel(
            name='Favourite_Music',
        ),
        migrations.DeleteModel(
            name='Playlist_Music',
        ),
    ]
