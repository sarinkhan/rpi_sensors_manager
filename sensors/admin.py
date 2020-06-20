from django.contrib import admin

# Register your models here.
from .models import Sensor, Measures, ProbeDriver

admin.site.register(Sensor)
admin.site.register(Measures)
admin.site.register(ProbeDriver)
