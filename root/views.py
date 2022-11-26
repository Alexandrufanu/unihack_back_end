from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response

from root.serializers import UserSerializer, GroupSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.views import APIView


@api_view(["GET", "POST"])
def user_list(request):
    # get users

    if request.method == "GET":
        users = User.objects.all()
        serializer = UserSerializer(users, many=True, context={'request': request})

        # return JsonResponse({"data": serializer.data})  # no need for safe here
        return JsonResponse({"data": serializer.data}, safe=False)

    if request.method == "POST":
        serializer = UserSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors)



class UserViewSet(viewsets.ModelViewSet):  # APIView
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet, ):  # APIView
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    # queryset = {"AAAA":22}

    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

