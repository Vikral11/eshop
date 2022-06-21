# Generated by Django 4.0.4 on 2022-04-27 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('address1', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('address2', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('address3', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='main_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('address1', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('address2', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('address3', models.TextField(blank=True, default=None, max_length=100, null=True)),
                ('pin', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pic', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='sub_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('baseprice', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('final_price', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('stock', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('pic1', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic2', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic3', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('pic4', models.ImageField(blank=True, default=None, null=True, upload_to='media/images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.brand')),
                ('main_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.main_cat')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.seller')),
                ('sub_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.sub_cat')),
            ],
        ),
    ]