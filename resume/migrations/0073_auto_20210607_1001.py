# Generated by Django 3.1 on 2021-06-07 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0072_auto_20210326_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meslanguageprogrammation',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '11. Mes languages Programmation'},
        ),
        migrations.AlterModelOptions(
            name='projecttype',
            options={'ordering': ['order', 'id'], 'verbose_name_plural': '12. ProjectTypes'},
        ),
        migrations.AddField(
            model_name='personalinfo',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='meslanguageprogrammation',
            name='level',
            field=models.IntegerField(choices=[(5, 'Expert'), (4, 'Advanced'), (3, 'Intermediate'), (2, 'Novice'), (1, 'Fundamental Awareness')], default=1, help_text='Choice between 1 and 5'),
        ),
    ]