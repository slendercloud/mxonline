# Generated by Django 2.0.2 on 2018-04-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userask',
            name='mobile',
            field=models.CharField(default='', max_length=11, verbose_name='手机号'),
        ),
    ]
