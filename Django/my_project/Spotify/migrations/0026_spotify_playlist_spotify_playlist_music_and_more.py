# Generated by Django 4.2.1 on 2023-05-13 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0025_delete_spotify_playlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='spotify_playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='photos/spotify_playlist')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='spotify_playlist_Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.music')),
                ('spotify_playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.spotify_playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Playlist_Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.music')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite_Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.music')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.user')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite_Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.user')),
            ],
        ),
    ]
