# Generated by Django 2.2.1 on 2019-06-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empire', '0002_auto_20190602_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='username',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
