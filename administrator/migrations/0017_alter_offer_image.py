# Generated by Django 3.2.5 on 2022-05-14 16:19

import administrator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0016_alter_offer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(default=administrator.get_offer_image, upload_to='offers/'),
        ),
    ]
