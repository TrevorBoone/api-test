from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Activity

from .serializers import ActivitySerializer

# Create your views here.
class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows activities to be viewed or edited.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    # permission_classes = [permissions.IsAuthenticated]