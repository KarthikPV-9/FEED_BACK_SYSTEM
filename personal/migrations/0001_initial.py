# Generated by Django 4.0.3 on 2022-03-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('enrollment_no', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=50)),
            ],
        ),
    ]
