# Generated by Django 4.0.3 on 2022-04-10 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='publicp',
            field=models.BooleanField(default=True),
        ),
    ]
