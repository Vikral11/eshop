# Generated by Django 4.0.4 on 2022-05-26 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0027_checkoutproducts_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutproducts',
            name='buyer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainApp.buyer'),
            preserve_default=False,
        ),
    ]
