# Generated by Django 3.0.5 on 2020-04-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Wanted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_number', models.CharField(blank=True, default='', max_length=20, null=True)),
            ],
            options={
                'ordering': ['-publish_time'],
            },
        ),
    ]