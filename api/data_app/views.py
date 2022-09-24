from rest_framework import generics, permissions
from rest_framework.response import Response

from api.utils import threat_utils


class ThreatApi(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, *args, **kwargs):
        anomalies = threat_utils.get_anomalies()

        return Response({
            "anomalies": anomalies,
            "message": "Anomalies retrieved successfully."
        })
