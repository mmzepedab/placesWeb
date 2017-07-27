from django.contrib.auth.models import User, Group
from .models import Place, AppUser, Offer, PlaceSubscriber
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.db import models
from django.conf import settings



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
    is_user_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Place
        fields = ('name', 'address', 'email', 'phone_number', 'description', 'image', 'image_thumbnail', 'image_cover', 'offers', 'subscriber_count', 'is_user_subscribed')

    def get_subscriber_count(self, obj):
        return obj.subscribers.count()

    def get_is_user_subscribed(self, obj):
        is_user_subscribed = self.context.get("is_user_subscribed")
        return is_user_subscribed

class AppUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id', 'full_name', 'first_name', 'last_name', 'email', 'facebook_id', 'profile_picture', 'push_token', 'ionic_id')



class OfferSerializer(serializers.HyperlinkedModelSerializer):
    place_name = serializers.SerializerMethodField()
    def get_place_name(self, obj):
        return obj.place.name

    place_subscribers_count = serializers.SerializerMethodField()
    def get_place_subscribers_count(self, obj):
        return obj.place.subscribers.count()

    place_image_thumbnail = serializers.SerializerMethodField()
    def get_place_image_thumbnail(self, obj):
        request = self.context.get('request')
        return 'http://%s%s%s' % (request.get_host(), settings.MEDIA_URL, obj.place.image_thumbnail)

    class Meta:
        model = Offer
        fields = ('name', 'description', 'start_date', 'end_date', 'place', 'place_name', 'place_image_thumbnail', 'place_subscribers_count' ,'offer_type', 'image_thumbnail','image')



class PlaceSubscriberSerializer(serializers.ModelSerializer):
    place = PlaceSerializer(required=False)
    user = AppUserSerializer(required=False)
    date_subscribed = serializers.DateField(required=False)
    class Meta:
        model = PlaceSubscriber
        fields = ('id', 'place', 'user', 'date_subscribed')

    def get_validation_exclusions(self):
        exclusions = super(PlaceSubscriberSerializer, self).get_validation_exclusions()
        return exclusions + ['place', 'user', 'date_subscribed']