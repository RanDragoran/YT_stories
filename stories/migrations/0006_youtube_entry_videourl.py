# Generated by Django 3.0.7 on 2020-07-10 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20200710_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube_entry',
            name='videoUrl',
            field=models.URLField(null=True),
        ),
    ]
