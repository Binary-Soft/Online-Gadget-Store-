# Generated by Django 3.2.4 on 2022-07-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productstemplate', '0021_alter_notice_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, default=''),
        ),
    ]