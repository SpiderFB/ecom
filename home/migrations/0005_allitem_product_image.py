# Generated by Django 5.0.1 on 2024-01-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_rename_price_allitem_product_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allitem',
            name='product_image',
            field=models.ImageField(default='default_image.jpg', upload_to='static/images/'),
        ),
    ]
