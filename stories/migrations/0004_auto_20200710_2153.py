# Generated by Django 3.0.7 on 2020-07-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20200710_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentstories',
            name='commentKey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_content', to='stories.Youtube_Entry'),
        ),
    ]
