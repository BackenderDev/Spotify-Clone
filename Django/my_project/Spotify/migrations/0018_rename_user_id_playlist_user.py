# Generated by Django 4.2.1 on 2023-05-12 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0017_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='user_id',
            new_name='user',
        ),
    ]
