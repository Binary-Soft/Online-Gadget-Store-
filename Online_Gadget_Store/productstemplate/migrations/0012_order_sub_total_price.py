# Generated by Django 3.2.4 on 2022-07-13 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productstemplate', '0011_order_is_last'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='sub_total_price',
            field=models.FloatField(default=0.0),
        ),
    ]
