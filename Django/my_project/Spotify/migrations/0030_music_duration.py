# Generated by Django 4.2.1 on 2023-05-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spotify', '0029_alter_user_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='duration',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
