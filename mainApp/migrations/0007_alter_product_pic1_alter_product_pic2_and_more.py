# Generated by Django 4.0.4 on 2022-05-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_alter_seller_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/productimages/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='media/productimages/'),
        ),
    ]
