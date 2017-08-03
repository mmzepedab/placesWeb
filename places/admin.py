from django.contrib import admin

# Register your models here.
from .models import Category, Place, Offer, AppUser, PlaceSubscriber

class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(Category)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Offer)
admin.site.register(AppUser)
admin.site.register(PlaceSubscriber)
