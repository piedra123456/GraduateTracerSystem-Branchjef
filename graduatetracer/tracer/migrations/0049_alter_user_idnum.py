# Generated by Django 4.1.1 on 2022-09-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracer', '0048_delete_systemuser_alter_advertise_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='IDNum',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
