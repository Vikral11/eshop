# Generated by Django 4.0.4 on 2022-05-11 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_product_pic1_alter_product_pic2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='pin',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='state',
            field=models.CharField(blank=True, default=None, max_length=20, null=True),
        ),
    ]
