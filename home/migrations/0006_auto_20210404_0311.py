# Generated by Django 3.1.7 on 2021-04-03 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210404_0300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient',
            new_name='Record',
        ),
    ]
