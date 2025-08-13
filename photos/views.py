from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Photo
from .serializers import PhotoSerializer

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [MultiPartParser, FormParser] 
