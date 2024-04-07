from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from my_app.models import User, Client
from .serializers import UserSerializers, ClientSerializers, PostSerializers
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.viewsets import ModelViewSet




class UserView(ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ClientView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class ClientDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class PostView(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = PostSerializers


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = PostSerializers
