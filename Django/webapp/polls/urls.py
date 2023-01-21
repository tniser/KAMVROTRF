from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/', views.cats, name='cats'),
    path('cats/<slug:catid>/', views.cats, name='cats_category')
]