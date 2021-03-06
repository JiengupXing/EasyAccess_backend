# Generated by Django 3.0.5 on 2020-04-03 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('submit_time', models.DateTimeField(auto_now=True)),
                ('belong_to_grade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_of_grade', to='myauth.Grade')),
                ('submitter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course_who_submit', to='myauth.User')),
            ],
            options={
                'ordering': ['-submit_time'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icons', verbose_name='图标')),
                ('download_url', models.URLField()),
                ('belong_to_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tools_of_course', to='download.Course')),
            ],
        ),
    ]
