# Generated by Django 5.1.2 on 2024-12-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inentory_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceprouct',
            name='display_size',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='deviceprouct',
            name='weight',
            field=models.FloatField(),
        ),
    ]
