from django.contrib.auth.models import User, Group
from .models import Place, AppUser
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import models



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    offers = serializers.StringRelatedField(many=True)
    class Meta:
        model = Place
        fields = ('name', 'description', 'image', 'image_thumbnail', 'image_cover', 'offers')

class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('full_name', 'first_name', 'last_name', 'email', 'facebook_id', 'profile_picture')