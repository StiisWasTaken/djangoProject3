from django.urls import path
from .views import (PostListView, PostDetailView,PostCreateView,PostUpdateView,PostDelateView,BikeDetailView,AccesorDetailView)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),             #  blog\ bo '' jest puste a apka nazywa sie blog
    path('bikes/', views.bikes, name='blog-bikes'),     # blog\bike
    path('bikes/<int:pk>/', BikeDetailView.as_view(), name='bikes-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDelateView.as_view(), name='post-delete'),
    path('parts', views.parts, name='blog-parts'),
    path('accesories',views.accesories, name='blog-accesories'),
    path('accesories/<int:pk>/',AccesorDetailView.as_view(), name='accesories-detail'),
    path('rent',views.rent, name='blog-rent'),
    #path('profile', views.profile, name='blog-profile'),
    path('cart', views.cart, name='blog-cart'),
]

