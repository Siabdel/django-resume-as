# Generated by Django 2.0.3 on 2018-03-31 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0044_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
