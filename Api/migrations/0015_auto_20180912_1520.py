# Generated by Django 2.0.6 on 2018-09-12 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0014_auto_20180912_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='user',
        ),
        migrations.AlterField(
            model_name='park',
            name='record_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.User'),
        ),
    ]
