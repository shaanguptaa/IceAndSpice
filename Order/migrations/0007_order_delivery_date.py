# Generated by Django 3.2.5 on 2022-04-28 22:48

import IceAndSpice
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=IceAndSpice.get_datetime),
        ),
    ]
