from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),             #  blog\ bo '' jest puste a apka nazywa sie blog
    path('bikes/', views.bikes, name='blog-bikes'),     # blog\bike
    path('parts', views.parts, name='blog-parts'),
    path('accesories',views.accesories, name='blog-accesories'),
    path('rent',views.rent, name='blog-rent'),
    path('profile', views.profile, name='blog-profile'),
    path('cart', views.cart, name='blog-cart'),
]