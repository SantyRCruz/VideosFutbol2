# Generated by Django 3.1.7 on 2021-04-11 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='foto',
            new_name='Escudo',
        ),
    ]
