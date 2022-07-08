# Generated by Django 4.0.3 on 2022-03-23 13:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_faculty_username'),
        ('feedback', '0002_alter_feedback_content_alter_feedback_course_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='date_submitted'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='feedback',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.student'),
        ),
    ]