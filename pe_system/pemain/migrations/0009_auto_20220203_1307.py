# Generated by Django 3.2.8 on 2022-02-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemain', '0008_borrow_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipments',
            name='available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='borrowed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='equipments',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
