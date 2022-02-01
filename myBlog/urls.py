from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path('article_list/', views.article_list, name='article_list'),
    path('article_details/', views.article_details, name='article_details'),

]
