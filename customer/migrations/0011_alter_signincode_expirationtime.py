# Generated by Django 4.0.3 on 2022-08-04 08:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_signincode_expirationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signincode',
            name='expirationTime',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 8, 11, 27, 817317, tzinfo=utc)),
        ),
    ]
