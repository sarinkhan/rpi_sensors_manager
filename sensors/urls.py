from django.urls import path

from . import views

app_name = 'sensors'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='sensor_detail'),
    path('sensor/<int:pk>/', views.DetailView.as_view(), name='detail'),
]

"""
path('', views.index, name='index'),
path('sensor2/<int:pk>/', views.DetailView.as_view(), name='detail'),
path('probedriver/<str:probe_driver_id>/', views.view_probe_driver,
name='view_probe_driver'),"""
