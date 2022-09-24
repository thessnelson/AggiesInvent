from django.urls import path, include

from .views import ThreatApi

urlpatterns = [
    path('threat-data/', ThreatApi.as_view(), name='threat-data')
]
