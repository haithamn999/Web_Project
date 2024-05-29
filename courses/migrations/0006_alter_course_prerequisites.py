# Generated by Django 5.0.4 on 2024-05-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_prerequisites_alter_course_scheduled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisites',
            field=models.CharField(blank=True, choices=[('Object Oriented Programming', 'Object Oriented Programming'), ('Web Programming', 'Web Programming'), ('Discrete Mathematics', 'Discrete Mathematics'), ('Calculus 1', 'Calculus 1'), ('Calculus 2', 'Calculus 2'), ('', ''), ('Data Structure', 'Data Structure'), ('Computer Programming', 'Computer Programming')], max_length=200, null=True),
        ),
    ]
