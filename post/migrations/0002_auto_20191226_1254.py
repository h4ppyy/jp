# Generated by Django 3.0.1 on 2019-12-26 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='post',
        ),
        migrations.AlterModelTable(
            name='postinfo',
            table='post_info',
        ),
    ]
