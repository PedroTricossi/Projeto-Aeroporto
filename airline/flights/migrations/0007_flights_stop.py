# Generated by Django 3.0.6 on 2020-05-18 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0006_remove_flights_stops'),
    ]

    operations = [
        migrations.AddField(
            model_name='flights',
            name='stop',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='stop', to='flights.Airport'),
        ),
    ]