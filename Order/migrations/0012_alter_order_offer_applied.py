# Generated by Django 3.2.5 on 2022-05-13 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0009_offer_items'),
        ('Order', '0011_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='offer_applied',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.offer'),
        ),
    ]