# Generated by Django 3.0.7 on 2020-06-17 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0005_probedriver'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='probe_driver',
            field=models.ForeignKey(default='driverName', on_delete=django.db.models.deletion.CASCADE, to='sensors.ProbeDriver'),
        ),
    ]
