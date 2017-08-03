from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class AppUser(models.Model):
    full_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    facebook_id = models.CharField(max_length=200, unique=True, error_messages={'unique':"This User Already Registered"})
    profile_picture = models.CharField(max_length=500)
    push_token = models.CharField(max_length=200, default=0)
    ionic_id = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_blocked = models.BooleanField(default=False)
    #my_places = models.ManyToManyField(Place, through='PlaceSubscriber')

    def __str__(self):
        return self.full_name


class Place(models.Model):
    PLACE_TYPES = (
		(1, 'Restaurant'),
		(2, 'Bar'),
		(3, 'Bar and Restaurant'),
    )
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    #city_id = models.CharField(max_length=200)
    place_type_id = models.IntegerField(default=1, choices=PLACE_TYPES)
    #image = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    image_thumbnail = models.ImageField(upload_to='images/thumbnails')
    image_cover = models.ImageField(upload_to='images/covers')
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places', default=1)
    subscribers = models.ManyToManyField(AppUser, through='PlaceSubscriber')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):              # __unicode__ on Python
   		return self.name


class Offer(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    place = models.ForeignKey(Place, related_name='offers', on_delete=models.CASCADE)
    offer_type = models.IntegerField(default=0)
    image_thumbnail = models.ImageField(upload_to='images/thumbnails')
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
    	return self.name

	class Meta:
		ordering = ('name',)


class PlaceSubscriber(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        unique_together = ('place', 'user')

    def __str__(self):
        return '%s %s' % (self.place, self.user)