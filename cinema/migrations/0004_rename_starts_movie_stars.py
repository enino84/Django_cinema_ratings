# Generated by Django 4.0.3 on 2022-04-10 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0003_alter_movie_release'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='starts',
            new_name='stars',
        ),
    ]