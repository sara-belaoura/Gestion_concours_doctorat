# Generated by Django 3.2.3 on 2021-06-16 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210616_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='copie',
            name='isvalidated',
        ),
    ]