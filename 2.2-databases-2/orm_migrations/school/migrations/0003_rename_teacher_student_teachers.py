# Generated by Django 4.0.2 on 2022-02-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_remove_student_teacher_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
