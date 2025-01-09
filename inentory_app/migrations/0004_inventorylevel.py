# Generated by Django 5.1.2 on 2024-12-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inentory_app', '0003_totalproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_summaries', models.CharField(max_length=200)),
                ('stuff', models.CharField(max_length=100)),
                ('stock_type', models.CharField(max_length=100)),
                ('stock_range', models.IntegerField(max_length=100)),
                ('sales_num', models.IntegerField(max_length=100)),
                ('lastdate', models.DateField()),
            ],
        ),
    ]
