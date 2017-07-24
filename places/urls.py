from django.conf.urls import url, include

from . import views

from views import PlaceOffersList

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'appUsers', views.AppUserViewSet)
router.register(r'placeOffers', views.PlaceOffersList, 'place_offers')

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/create/$', views.category_create, name='create_category'),
    url(r'^category/list/$', views.category_list, name='list_category'),
    url(r'^place/list/$', views.place_list, name='list_place'),
    url(r'^place/create/$', views.place_create, name='create_place'),
    url(r'^place/update/(?P<pk>\d+)$', views.place_update, name='update_place'),
    url(r'^place/(?P<pk>\d+)$', views.PlaceDetailView.as_view(), name='detail_place'),
    url(r'^place/delete/(?P<pk>\d+)/$', views.place_delete, name='delete_place'),
    # Offer urls
    url(r'^place/(?P<pk>\d+)/offer/create/$', views.add_offer_to_place, name='add_offer_to_place'),
    url(r'^offer/create/$', views.offer_create, name='create_offer'),
    url(r'^offer/(?P<pk>\d+)$', views.OfferDetailView.as_view(), name='detail_offer'),
    url(r'^offer/delete/(?P<pk>\d+)/$', views.offer_delete, name='delete_offer'),
    url(r'^placeSubscriber/delete/$', views.place_subscriber_delete, name='delete_place_subscriber'),
    #url(r'^api/place/(?P<place_id>.+)/offers/$', PlaceOffersList.as_view(), name='place_offer_view'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]