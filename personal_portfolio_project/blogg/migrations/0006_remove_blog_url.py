# Generated by Django 3.0.7 on 2020-06-13 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0005_auto_20200613_1853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='url',
        ),
    ]
