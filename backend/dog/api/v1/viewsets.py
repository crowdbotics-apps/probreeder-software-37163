from rest_framework import authentication
from dog.models import Dog
from .serializers import DogSerializer
from rest_framework import viewsets


class DogViewSet(viewsets.ModelViewSet):
    serializer_class = DogSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Dog.objects.all()
