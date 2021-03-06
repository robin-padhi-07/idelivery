# Generated by Django 2.2.6 on 2019-11-20 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemMeasuementUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('name', models.CharField(default='NONE', max_length=50, null=True, unique=True)),
                ('note', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default=('AT', 'ACTIVE'), max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('order_id', models.CharField(max_length=15, unique=True)),
                ('delivery_charges', models.FloatField(default=1.0, max_length=5)),
                ('status_note', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(choices=[('OPD', 'ORDER_PLACED'), ('OCC', 'ORDER_CONFIRMED_BY_CUSTOMER'), ('OPU', 'ORDER_PICKEDUP'), ('ODD', 'ORDER_DELIVERED'), ('OCD', 'ORDER_CANCELLED')], default=('OPD', 'ORDER_PLACED'), max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, upload_to='media/profile_pics')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('ref_id', models.CharField(max_length=15, unique=True)),
                ('phone_primary', models.CharField(default='NONE', max_length=10)),
                ('phone_secondary', models.CharField(default='NONE', max_length=10)),
                ('location_area', models.CharField(default='NONE', max_length=80)),
                ('location_sublocality', models.CharField(default='NONE', max_length=80)),
                ('location_locality', models.CharField(default='NONE', max_length=80)),
                ('location_city', models.CharField(default='NONE', max_length=80)),
                ('location_state', models.CharField(default='KERALA', max_length=80)),
                ('location_pincode', models.CharField(default='NONE', max_length=6)),
                ('user_type', models.CharField(choices=[('SR', 'SUPER_ADMIN'), ('MR', 'MANAGER'), ('CR', 'CONSUMER'), ('DR', 'DELIVERY_AGENT'), ('BO', 'BUSINESS_OWNER')], default=('SR', 'SUPER_ADMIN'), max_length=2)),
                ('user_status', models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default=('AT', 'ACTIVE'), max_length=2)),
                ('status', models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default=('AT', 'ACTIVE'), max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('order_item_id', models.CharField(max_length=15, unique=True)),
                ('item_name', models.CharField(max_length=60)),
                ('item_quantity', models.PositiveSmallIntegerField(default=1)),
                ('item_price', models.FloatField(default=1.0, max_length=5)),
                ('status_note', models.CharField(max_length=200, unique=True)),
                ('status', models.CharField(choices=[('IPD', 'O_ITEM_PICKED'), ('INA', 'O_ITEM_NOT_AVAILABLE'), ('IRD', 'O_ITEM_REMOVED'), ('IRJ', 'O_ITEM_REJECTED')], default=('IPD', 'O_ITEM_PICKED'), max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('measurement_unit', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='measurement_unit', to='base_app.ItemMeasuementUnit')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_customer',
            field=models.ForeignKey(limit_choices_to={'user_type': 'CR'}, on_delete=django.db.models.deletion.CASCADE, related_name='user_customer', to='base_app.UserProfileInfo'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_delivery_agent',
            field=models.ForeignKey(limit_choices_to={'user_type': 'DR'}, on_delete=django.db.models.deletion.CASCADE, related_name='user_delivery_agent', to='base_app.UserProfileInfo'),
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=8, unique=True)),
                ('business_nature', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('AT', 'ACTIVE'), ('IA', 'INACTIVE'), ('DS', 'DISABLED'), ('DL', 'DELETED')], default=('AT', 'ACTIVE'), max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(limit_choices_to={'user_type': 'BO'}, on_delete=django.db.models.deletion.CASCADE, related_name='user_business', to='base_app.UserProfileInfo')),
            ],
        ),
    ]
