# Generated by Django 2.2.1 on 2019-06-02 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empire', '0003_auto_20190602_1151'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserLogin',
            new_name='User',
        ),
    ]
