# Generated by Django 4.1.1 on 2022-12-13 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta_fetch', '0005_csv_j_son_userjson'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='I_mage',
            new_name='ImageData',
        ),
        migrations.RenameModel(
            old_name='J_son',
            new_name='JsonData',
        ),
    ]
