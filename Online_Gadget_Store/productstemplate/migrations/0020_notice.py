# Generated by Django 3.2.4 on 2022-07-21 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productstemplate', '0019_auto_20220721_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField(max_length=120)),
            ],
        ),
    ]