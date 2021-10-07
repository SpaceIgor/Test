from django.contrib.auth.models import User, Group
from rest_framework import permissions
from tutorial.quickstart.serializers import *
from tutorial.quickstart.models import *
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonView(viewsets.ModelViewSet):
    """
    API endpoint that allows person to be viewed, added, edited and deleted
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

