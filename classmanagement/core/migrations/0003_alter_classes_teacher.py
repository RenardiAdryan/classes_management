# Generated by Django 4.2.9 on 2024-01-09 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_classes_student_classes_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
    ]
