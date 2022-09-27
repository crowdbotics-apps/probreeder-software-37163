from rest_framework import authentication
from kennel.models import Kennel
from .serializers import KennelSerializer
from rest_framework import viewsets


class KennelViewSet(viewsets.ModelViewSet):
    serializer_class = KennelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Kennel.objects.all()
