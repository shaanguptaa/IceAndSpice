# Generated by Django 3.2.5 on 2022-05-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0010_order_offer_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
