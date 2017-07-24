from django.contrib.auth.models import User, Group
from .models import Place, AppUser, Offer
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

    subscriber_count = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('id', 'name', 'address', 'email', 'phone_number', 'description', 'image', 'image_thumbnail', 'image_cover', 'offers', 'subscriber_count')

    def get_subscriber_count(self, obj):
        return obj.subscribers.count()

class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('full_name', 'first_name', 'last_name', 'email', 'facebook_id', 'profile_picture')



class OfferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Offer
        fields = ('name', 'description', 'start_date', 'end_date', 'place', 'offer_type', 'image_thumbnail','image')