from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Sensor, Measures, ProbeDriver
from django.utils import timezone


class SensorsList(generic.ListView):
    template_name = 'sensors/sensors_list.html'
    context_object_name = 'latest_sensor_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors_count'] = Sensor.objects.all().count()
        return context

    def get_queryset(self):
        """Return the last 20 configured sensors."""
        return Sensor.objects.order_by('id')[:20]


class ProbesList(generic.ListView):
    template_name = 'sensors/probes_list.html'
    context_object_name = 'latest_probes_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['probes_count'] = ProbeDriver.objects.all().count()
        return context

    def get_queryset(self):
        """Return the last 20 probes."""
        return ProbeDriver.objects.order_by('name')[:20]

class SensorDetailView(generic.DetailView):
    model = Sensor
    template_name = 'sensors/sensor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['last'] = Measures.objects.filter(sensor_id=context['sensor'].id).order_by("-ts")[0]
        context['probe'] = ProbeDriver.objects.get(name=context['sensor'].probe_driver)
        context['measures_count'] = Measures.objects.filter(sensor_id=context['sensor'].id).count()
        return context


class IndexView(generic.ListView):
    template_name = 'sensors/index.html'
    context_object_name = 'latest_sensor_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sensors_count'] = Sensor.objects.all().count()
        return context

    def get_queryset(self):
        """Return the last five saved sensors."""
        return Sensor.objects.order_by('-id')[:4]

"""
def view_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor})
def view_probe_driver(request, probe_driver_id):
    return HttpResponse("You're looking at probe driver %s." % probe_driver_id)
"""
