# Generated by Django 3.1.13 on 2022-08-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0002_auto_20210717_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='resourceId',
            field=models.CharField(default='a', max_length=1, unique=True),
            preserve_default=False,
        ),
    ]