from .models import songModel, singerModel
from .serializers import songModelSerializer, singerModelSerializer

from rest_framework import viewsets



class singerInformation_API(viewsets.ModelViewSet):
    queryset            = singerModel.objects.all()
    serializer_class    = singerModelSerializer


class songInformation_API(viewsets.ModelViewSet):
    queryset = songModel.objects.all()
    serializer_class = songModelSerializer