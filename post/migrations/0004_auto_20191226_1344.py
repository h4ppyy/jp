# Generated by Django 3.0.1 on 2019-12-26 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20191226_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='delete_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='postinfo',
            name='delete_data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
