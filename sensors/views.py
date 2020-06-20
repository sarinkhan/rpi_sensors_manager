from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Sensor, Measures, ProbeDriver
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'sensors/sensor_index.html'
    context_object_name = 'latest_sensor_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Sensor.objects.order_by('-name')[:20]

class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'sensors/sensor_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['last'] = Measures.objects.filter(sensor_id=context['sensor'].id).order_by("-ts")[0]
        context['probe'] = ProbeDriver.objects.get(name=context['sensor'].probe_driver)
        context['measures_count'] = Measures.objects.filter(sensor_id=context['sensor'].id).count()
        return context


"""
def view_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor})
def view_probe_driver(request, probe_driver_id):
    return HttpResponse("You're looking at probe driver %s." % probe_driver_id)
"""
