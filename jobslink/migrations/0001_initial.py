# Generated by Django 2.1.5 on 2020-01-15 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDesc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
                ('uniq_id', models.CharField(max_length=50)),
                ('job_description', models.TextField(max_length=1000)),
                ('post_date', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('contact_email', models.EmailField(max_length=50)),
            ],
        ),
    ]