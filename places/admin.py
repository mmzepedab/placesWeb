from django.contrib import admin

# Register your models here.
from .models import Category, Place, Offer, AppUser, PlaceSubscriber

admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Offer)
admin.site.register(AppUser)
admin.site.register(PlaceSubscriber)
