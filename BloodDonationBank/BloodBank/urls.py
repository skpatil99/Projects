from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^beforeSearch/',views.beforeSearch,name='beforeSearch'),
    url(r'^search/',views.search,name='search'),
    url('', include('django.contrib.auth.urls')),

    url(r'^donorRegistration/',views.donorRegistration,name='donorRegistration'),
    url(r'^getDonorRegInfo/',views.getDonorRegInfo,name='getDonorRegInfo'),

    url(r'^login/',auth_views.login,name='login'),
    url(r'^logout/',auth_views.logout,name='logout'),
    url(r'^newUser/',views.newUser,name='newUser'),
    url(r'^staff/',views.staff,name='staff'),

    url(r'^insertStock/',views.insertStock,name='insertStock'),
    url(r'^stockInfo/',views.stockInfo,name='stockInfo'),

    url(r'^donorInfo/',views.donorInfo,name='donorInfo'),
    url(r'^getDonorInfo/',views.getDonorInfo,name='getDonorInfo'),
    url(r'^getNewUserInfo/',views.getNewUserInfo,name='getNewUserInfo'),

]
