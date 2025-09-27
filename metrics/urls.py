from django.urls import path
from . import views

urlpatterns = [
    path("", views.metrics_base, name="metrics_base"),
]
