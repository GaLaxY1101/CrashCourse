# Generated by Django 3.2 on 2021-04-24 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_product_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone_numer',
            new_name='phone_number',
        ),
    ]
