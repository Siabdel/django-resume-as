# Generated by Django 2.0.2 on 2018-03-08 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0028_personalinfo_suffix'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '13. Achievements'},
        ),
        migrations.AlterModelOptions(
            name='language',
            options={'ordering': ['level', 'order'], 'verbose_name_plural': '10. Languages'},
        ),
        migrations.AlterModelOptions(
            name='programmingarea',
            options={'ordering': ['order', 'name'], 'verbose_name_plural': '08. Programming areas'},
        ),
        migrations.AlterModelOptions(
            name='programminglanguage',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '09. Programming languages'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '11. Projects'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-year', 'order'], 'verbose_name_plural': '14. Publications'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '07. Skills'},
        ),
        migrations.AlterModelOptions(
            name='skillset',
            options={'ordering': ['id'], 'verbose_name_plural': '06. Skillsets'},
        ),
    ]
