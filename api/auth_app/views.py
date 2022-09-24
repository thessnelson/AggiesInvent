from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer

class UserView(GenericAPIView):
    serializer_class = UserSerializer