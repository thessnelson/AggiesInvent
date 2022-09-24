from rest_framework import generics, permissions
from rest_framework.response import Response

from api.utils import threat_utils


class ThreatApi(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request, *args, **kwargs):
        threats = threat_utils.get_threats()

        return Response({
            "threats": threats,
            "message": "Threats retrieved successfully."
        })
