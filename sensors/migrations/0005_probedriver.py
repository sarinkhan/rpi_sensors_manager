# Generated by Django 3.0.7 on 2020-06-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0004_auto_20200617_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProbeDriver',
            fields=[
                ('name', models.CharField(default='driverName', max_length=255, primary_key=True, serialize=False, verbose_name='name of the driver')),
                ('description', models.CharField(blank=True, max_length=2048, verbose_name='descripton of the driver')),
            ],
        ),
    ]
