# Generated by Django 3.0.7 on 2020-07-15 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=200)),
                ('blogContent', models.TextField()),
                ('blogDate', models.DateTimeField()),
                ('blogWriter', models.CharField(max_length=100)),
            ],
        ),
    ]
