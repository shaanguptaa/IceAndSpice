# Generated by Django 3.2.5 on 2022-04-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_order_delivery_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True),
        ),
    ]
