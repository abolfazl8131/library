# Generated by Django 4.0.3 on 2022-08-04 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_alter_signincode_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signincode',
            name='expirationTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 7, 55, 33, 732873, tzinfo=utc), verbose_name='expiration time (of ad)'),
        ),
    ]
