from rest_framework import serializers
from my_app.models import User, Client
from django.contrib.auth import get_user_model


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # Hamma malumotlarni oladi
        # fields = ('UserName', 'Password') # Ozimizga kerakli malumotlar


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('FirstName', 'LastName', 'CarModel', 'CarNumber', 'PhoneNumber', 'CreatedUserId') # Ozimizga kerakli malumotlar


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'