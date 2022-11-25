from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from root.serializers import UserSerializer, GroupSerializer

from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet, APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet, APIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]