# Generated by Django 5.1.1 on 2024-09-17 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_product_stock_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(error_messages={'required': True}, max_length=150),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(error_messages={'required': True}, max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, error_messages={'required': False}, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(error_messages={'required': True}),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock_available',
            field=models.IntegerField(error_messages={'required': True}),
        ),
    ]
