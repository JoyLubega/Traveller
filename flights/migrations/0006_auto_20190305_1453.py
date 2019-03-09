# Generated by Django 2.1.4 on 2019-03-05 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0005_booking_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='booking',
            name='passport_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]