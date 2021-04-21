from rest_framework import viewsets, permissions
from .models import Author, Manuscript, Volume, Sections
from .serializers import ManuscriptSerializer, AuthorSerializer, VolumeSerializer, SectionsSerializer
from django.db.models import Count


class ManuscriptViewSet(viewsets.ModelViewSet):
    queryset = Manuscript.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ManuscriptSerializer
    http_method_names = ['get']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer
    http_method_names = ['get']


class VolumeViewSet(viewsets.ModelViewSet):
    queryset = Volume.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VolumeSerializer
    http_method_names = ['get']


class SectionsViewSet(viewsets.ModelViewSet):
    queryset = Sections.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SectionsSerializer
    http_method_names = ['get']


class DegreeCount(viewsets.OrderedDict):
    qs = Author.objects.order_by('degree').values('degree').annotate(Count('id'))
    permission_classes = [
        permissions.AllowAny
    ]
    http_method_names = ['get']
