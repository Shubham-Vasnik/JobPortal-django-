# Generated by Django 2.1.5 on 2020-01-16 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=200)),
                ('news_link', models.CharField(max_length=80)),
                ('date', models.CharField(max_length=20)),
                ('image', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News_Blog',
            },
        ),
    ]