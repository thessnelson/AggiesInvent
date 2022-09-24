from django.urls import path, include

from .views import ThreatApi

urlpatterns = [
    path('api/threats/', ThreatApi.as_view(), name='list-threats')
]
