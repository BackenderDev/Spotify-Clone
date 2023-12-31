# Generated by Django 4.2.1 on 2023-05-08 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0010_delete_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.TextField(max_length=50)),
                ('album_description', models.TextField(max_length=100)),
                ('album_image', models.ImageField(upload_to='photos/album/')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Spotify.singer')),
            ],
        ),
    ]
