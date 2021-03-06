# Generated by Django 2.2.6 on 2019-11-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0006_auto_20191123_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='status',
            field=models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default='AT', max_length=2),
        ),
        migrations.AlterField(
            model_name='itemmeasuementunit',
            name='status',
            field=models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default='AT', max_length=2),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('OPD', 'ORDER_PLACED'), ('OCC', 'ORDER_CONFIRMED_BY_CUSTOMER'), ('OPU', 'ORDER_PICKEDUP'), ('ODD', 'ORDER_DELIVERED'), ('OCD', 'ORDER_CANCELLED')], default='OPD', max_length=3),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('IPL', 'O_ITEM_PLACED'), ('IPD', 'O_ITEM_PICKED'), ('INA', 'O_ITEM_NOT_AVAILABLE'), ('IRD', 'O_ITEM_REMOVED'), ('IRJ', 'O_ITEM_REJECTED')], default='IPL', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='status',
            field=models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default='AT', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_status',
            field=models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default='AT', max_length=2),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='user_type',
            field=models.CharField(choices=[('SR', 'SUPER_ADMIN'), ('MR', 'MANAGER'), ('CR', 'CONSUMER'), ('DR', 'DELIVERY_AGENT'), ('BO', 'BUSINESS_OWNER')], default='DR', max_length=2),
        ),
    ]
