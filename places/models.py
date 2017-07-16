from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.name


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
    def __str__(self):              # __unicode__ on Python
   		return self.name


class Offer(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	start_date = models.DateField()
	end_date = models.DateField()
	place = models.ForeignKey(Place, related_name='offers', on_delete=models.CASCADE)
	offer_type = models.IntegerField(default=0)
	image_thumbnail = models.ImageField(upload_to='images/thumbnails')
	image = models.ImageField(upload_to='images/')
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)