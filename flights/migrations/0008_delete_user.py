# Generated by Django 2.2 on 2019-04-18 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0007_delete_flights'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
