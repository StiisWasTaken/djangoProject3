from django.urls import path
from .views import (WpisLista, WpisSzczegoly,WpisTworzenie,WpisAktualizacja,WpisUsun,RowerSzczegoly,AkcesoriaSzczegoly)
from . import views


urlpatterns = [
    path('', WpisLista.as_view(), name='blog-home'),             #  blog\ bo '' jest puste a apka nazywa sie blog
    path('bikes/', views.bikes, name='blog-bikes'),     # blog\bike
    path('bikes/<int:pk>/', RowerSzczegoly.as_view(), name='bikes-detail'),
    path('post/<int:pk>/', WpisSzczegoly.as_view(), name='post-detail'),
    path('post/new/', WpisTworzenie.as_view(), name='post-create'),
    path('post/<int:pk>/update/', WpisAktualizacja.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', WpisUsun.as_view(), name='post-delete'),
    path('parts', views.parts, name='blog-parts'),
    path('accesories',views.accesories, name='blog-accesories'),
    path('accesories/<int:pk>/', AkcesoriaSzczegoly.as_view(), name='blog-accesories'),
    path('rent',views.rent, name='blog-rent'),
    #path('profile', views.profile, name='blog-profile'),
    path('cart', views.cart, name='blog-cart'),
]

