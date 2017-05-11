from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/create/$', views.category_create, name='create_category'),
    url(r'^category/list/$', views.category_list, name='list_category'),
    url(r'^place/list/$', views.place_list, name='list_place'),
    url(r'^place/create/$', views.place_create, name='create_place'),
    url(r'^place/(?P<pk>\d+)$', views.PlaceDetailView.as_view(), name='detail_place'),
]