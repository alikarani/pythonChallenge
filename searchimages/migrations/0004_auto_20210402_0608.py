# Generated by Django 3.1.7 on 2021-04-02 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchimages', '0003_auto_20210402_0548'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeoLocationList',
            new_name='list1',
        ),
        migrations.RenameField(
            model_name='list1',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='list1',
            old_name='lon',
            new_name='longitude',
        ),
    ]
