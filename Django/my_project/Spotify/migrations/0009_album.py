# Generated by Django 4.2.1 on 2023-05-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0008_delete_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_image', models.ImageField(upload_to='photos/album/')),
            ],
        ),
    ]
