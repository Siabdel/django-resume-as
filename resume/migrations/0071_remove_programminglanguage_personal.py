# Generated by Django 3.1 on 2021-03-24 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0070_auto_20210323_1026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programminglanguage',
            name='personal',
        ),
    ]
