# Generated by Django 3.0.7 on 2020-07-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ecommerce', '0007_auto_20200715_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='quantity',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
