# Generated by Django 3.0.7 on 2020-06-17 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0007_auto_20200617_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='probe_driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensors.ProbeDriver'),
        ),
    ]
