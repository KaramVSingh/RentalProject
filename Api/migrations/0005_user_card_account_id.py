# Generated by Django 2.0.6 on 2018-08-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_remove_partner_partner_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='card_account_id',
            field=models.CharField(default='a', max_length=50),
            preserve_default=False,
        ),
    ]
