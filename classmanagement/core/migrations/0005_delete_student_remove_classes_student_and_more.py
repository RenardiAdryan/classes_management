# Generated by Django 4.2.9 on 2024-01-10 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_student_user_remove_teacher_user_student_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='student',
        ),
        migrations.RemoveField(
            model_name='classes',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]