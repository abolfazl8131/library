# Generated by Django 4.0.3 on 2022-08-09 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('authors', models.TextField(null=True)),
                ('slug', models.SlugField()),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(db_index=True, max_length=100)),
                ('date_published', models.DateField()),
                ('published_no', models.SmallIntegerField()),
                ('book_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.bookclass')),
            ],
        ),
        migrations.AddField(
            model_name='bookclass',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.bookgenre'),
        ),
    ]
