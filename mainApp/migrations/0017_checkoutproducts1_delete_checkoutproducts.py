# Generated by Django 4.0.4 on 2022-05-19 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0016_remove_checkout_products_remove_checkoutproducts_q_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkoutproducts1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.IntegerField(default=1)),
                ('total', models.IntegerField(default=0)),
                ('checkout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.checkout')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.product')),
            ],
        ),
        migrations.DeleteModel(
            name='checkoutproducts',
        ),
    ]
