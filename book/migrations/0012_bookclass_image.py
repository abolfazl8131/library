# Generated by Django 4.0.3 on 2022-11-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_alter_bookclass_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookclass',
            name='image',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
