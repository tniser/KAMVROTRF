from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hours/', views.hours, name='hours'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_us, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('dbinfo/', views.dbinfo, name='dbinfo'),
]