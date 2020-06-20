from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.
from .models import Sensor


class IndexView(generic.ListView):
    template_name = 'sensors/sensor_index.html'
    context_object_name = 'latest_sensor_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Sensor.objects.order_by('-name')[:10]

class DetailView(generic.DetailView):
    model = Sensor
    template_name = 'sensors/sensor_detail.html'


"""
def view_sensor(request, sensor_id):
    sensor = get_object_or_404(Sensor, pk=sensor_id)
    return render(request, 'sensors/sensor_detail.html', {'sensor': sensor})
def view_probe_driver(request, probe_driver_id):
    return HttpResponse("You're looking at probe driver %s." % probe_driver_id)
"""
