# Generated by Django 4.0.3 on 2022-11-03 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('book', '0006_alter_bookobject_book_class_alter_bookobject_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookobject',
            name='book_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='book_class', to='book.bookclass'),
        ),
        migrations.AlterField(
            model_name='bookobject',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
