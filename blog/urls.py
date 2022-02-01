from . import views
from django.contrib import admin
from django.urls import path


app_name = 'blog'  # !  name of the app

urlpatterns = [
    path('', views.home,  name='home'),
    path('about', views.about, name='about'),
    path('social', views.social, name='social'),

    path('product', views.product_detail_view, name='detail'),
    path('create', views.product_create_view, name='create'),

    path('product/<int:id>/', views.dynamic_lookup_view, name='detail'),
    path('product_list', views.product_list_view, name='product_list')

]
