# Generated by Django 2.2.6 on 2019-11-20 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmeasuementunit',
            name='name',
            field=models.CharField(default='NONE', max_length=50, null=True),
        ),
    ]
