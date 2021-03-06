# Generated by Django 2.2.6 on 2019-11-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0002_auto_20191120_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('IPD', 'O_ITEM_PICKED'), ('INA', 'O_ITEM_NOT_AVAILABLE'), ('IRD', 'O_ITEM_REMOVED'), ('IRJ', 'O_ITEM_REJECTED'), ('IPL', 'O_ITEM_PLACED')], default=('IPD', 'O_ITEM_PICKED'), max_length=3),
        ),
    ]
