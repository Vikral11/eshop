# Generated by Django 4.0.4 on 2022-05-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_alter_product_stock_alter_seller_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='pic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/images/'),
        ),
    ]
