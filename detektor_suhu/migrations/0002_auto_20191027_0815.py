# Generated by Django 2.2.6 on 2019-10-27 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detektor_suhu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stats',
            old_name='temperature',
            new_name='suhu',
        ),
    ]
