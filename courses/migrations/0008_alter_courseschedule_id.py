# Generated by Django 5.0.4 on 2024-05-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_studentregistration_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseschedule',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
