# Generated by Django 3.2.4 on 2022-07-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productstemplate', '0020_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='announcement',
            field=models.TextField(max_length=255),
        ),
    ]