# Generated by Django 3.2.9 on 2021-11-14 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0002_rename_graduates_user_graduate'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CourseType',
            new_name='CourseGraduated',
        ),
        migrations.RenameModel(
            old_name='EmploymentStatus',
            new_name='GraduateStatus',
        ),
    ]
