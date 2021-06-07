from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns =[
    path('',views.gallery, name='gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/',views.addPhoto, name='add')
]