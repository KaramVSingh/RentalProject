# Generated by Django 2.0.6 on 2018-09-12 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0013_remove_sublettable_itinerary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('wash_requested', models.BooleanField(default=False)),
                ('detail_requested', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('auto_returned_on', models.DateTimeField(blank=True, null=True)),
                ('airport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Airport')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Auto')),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sublettable',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 15, 13, 37, 373127)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sublettable',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 12, 15, 13, 46, 227449)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='record_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_user_itinerary', to='Api.User'),
        ),
        migrations.AlterField(
            model_name='itinerary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_user_itinerary', to='Api.User'),
        ),
        migrations.AddField(
            model_name='park',
            name='itinerary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Itinerary'),
        ),
        migrations.AddField(
            model_name='park',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Partner'),
        ),
        migrations.AddField(
            model_name='park',
            name='record_creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='origin_user_park', to='Api.User'),
        ),
        migrations.AddField(
            model_name='park',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_user_park', to='Api.User'),
        ),
    ]
