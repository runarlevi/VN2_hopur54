# Generated by Django 3.0.6 on 2020-05-08 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='price',
            field=models.FloatField(default=0.99),
            preserve_default=False,
        ),
    ]
