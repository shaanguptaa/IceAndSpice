# Generated by Django 3.2.5 on 2022-04-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0002_auto_20220312_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('R', 'Reserved'), ('P', 'Pending'), ('C', 'Cancelled')], default='P', max_length=1),
        ),
    ]