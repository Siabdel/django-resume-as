# Generated by Django 3.1 on 2021-03-07 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0057_auto_20210210_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skillset',
            name='personal',
        ),
    ]
