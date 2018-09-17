# Generated by Django 2.0.6 on 2018-08-15 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('airport_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('airport_name', models.CharField(max_length=50)),
                ('valet_location', models.CharField(max_length=50)),
                ('minutes_pickup_delay_with_checkin', models.IntegerField(default=0)),
                ('minutes_pickup_delay_no_checkin', models.IntegerField(default=0)),
                ('rate_park_day', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_rent_day', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_wash', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_detail', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_basic_cleaning_for_sublet', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_itinerary_change_return_to_owner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_itinerary_change_per_mile_over_30_miles', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_park', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_terminal', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_fueling', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_itinerary_change_return', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_empty_trip', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_tax_1', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_tax_2', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_percent_sublet_paid_to_partner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_percent_sublet_paid_to_auto_owner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('promotion_points', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=50)),
                ('partner_tax_id', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('primary_number', models.CharField(max_length=50)),
                ('secondary_number', models.CharField(max_length=50)),
                ('has_wash', models.BooleanField(default=False)),
                ('has_detail', models.BooleanField(default=False)),
                ('partner_since', models.IntegerField(default=2018)),
                ('cumulative_points', models.IntegerField(default=0)),
                ('available_points', models.IntegerField(default=0)),
                ('partner_level', models.CharField(default='BASE', max_length=50)),
                ('partner_logo', models.ImageField(upload_to='')),
                ('rate_park_day', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_rent_day', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_wash', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_detail', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_basic_cleaning_for_sublet', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_itinerary_change_return_to_owner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_itinerary_change_per_mile_over_30_miles', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_park', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_terminal', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_fueling', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_itinerary_change_return', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_valet_commission_empty_trip', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_percent_sublet_paid_to_partner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('rate_percent_sublet_paid_to_auto_owner', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Airport')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('salt', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('primary_number', models.CharField(max_length=50)),
                ('secondary_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('license_expiration', models.DateField()),
                ('license_number', models.CharField(max_length=50)),
                ('license_state', models.CharField(max_length=50)),
                ('member_since', models.IntegerField(default=2018)),
                ('cumulative_points', models.IntegerField(default=0)),
                ('available_points', models.IntegerField(default=0)),
                ('email_validated', models.BooleanField(default=False)),
                ('partner', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Api.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.User')),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.User'),
        ),
    ]
