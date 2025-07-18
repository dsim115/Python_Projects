# Generated by Django 5.2.4 on 2025-07-17 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('course_number', models.IntegerField()),
                ('instructor_name', models.CharField(max_length=100)),
                ('duration', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'University Classes',
            },
        ),
    ]
