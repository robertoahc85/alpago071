# Generated by Django 5.1.3 on 2024-12-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_school_state'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='schools',
            field=models.ManyToManyField(related_name='students', to='school.school', verbose_name='Escuelas'),
        ),
    ]
