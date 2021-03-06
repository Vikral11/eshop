# Generated by Django 4.0.4 on 2022-05-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0024_remove_checkoutproducts_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkoutproducts',
            name='active',
        ),
        migrations.RemoveField(
            model_name='checkoutproducts',
            name='orderstatus',
        ),
        migrations.AddField(
            model_name='checkout',
            name='orderstatus',
            field=models.IntegerField(choices=[(1, 'Not Packed'), (2, 'Packed'), (3, 'Out For Delivery'), (4, 'Delivered')], default=1),
        ),
    ]
