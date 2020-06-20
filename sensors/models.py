from django.db import models


class Measures(models.Model):
    sensor_id = models.IntegerField()
    value = models.FloatField()
    ts = models.DateTimeField()

    def __str__(self):
        return "value: " + str(self.value)

    def was_published_recently(self):
        return self.ts >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        managed = False
        db_table = 'measures'


class ProbeDriver(models.Model):
    name = models.CharField('name of the driver', max_length=255,
                            primary_key=True)
    description = models.CharField('descripton of the driver', max_length=2048,
                                   blank=True)
    unit = models.CharField('measurement unit', max_length=255, blank=True)
    unit_symbol = models.CharField('symbol of the unit', max_length=255,
                                   blank=True)
    min_value = models.FloatField('lowest possible value', blank=True,
                                  null=True)
    max_value = models.FloatField('highest possible value', blank=True,
                                  null=True)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('user friendly name', max_length=255)
    description = models.CharField('description', max_length=2048, blank=True)
    probe_id = models.CharField('unique ID of the probe', max_length=1024,
                                default="0x00", blank=True)
    probe_driver = models.ForeignKey(ProbeDriver, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
