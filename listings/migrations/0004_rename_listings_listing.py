# Generated by Django 4.0.4 on 2022-05-16 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listings_num_ofbedroom'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]
