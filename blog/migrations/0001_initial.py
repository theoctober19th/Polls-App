# Generated by Django 2.0.7 on 2018-07-26 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('category', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('created', models.DateTimeField(verbose_name='Date Created')),
                ('modified', models.DateTimeField(verbose_name='Date modified')),
            ],
        ),
    ]
