# Generated by Django 4.0.3 on 2022-03-23 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, max_length=255)),
                ('course_rating', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=255)),
            ],
        ),
    ]
