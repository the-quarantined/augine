# Generated by Django 4.0.1 on 2022-07-31 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fashion', '0003_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='-1', max_length=127),
        ),
    ]
