# Generated by Django 4.0.3 on 2022-03-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemain', '0013_alter_registration_idnum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
