"""
Name of File: travel/urls
Brief description of the file: creates the urls for each travel app page 
Inputs: None
Outputs: None
"""
from django.urls import path, include
from . import views

#Urls list
urlpatterns = [
    path('select-region/', views.select_region, name='select_region'), #make /travel/select-region call views.select_region function
    path('recommend-attractions/', views.recommend_attractions, name='recommend_tourist_attractions'), #link recommend_attraction url with its function
    path('generate-schedule/', views.make_schedule, name='generate_schedule'), #link generate schedule url with its function
    path('recommend-restaurants/', views.recommend_restaurants, name='recommend_restaurants'), #link recommend restaurants url with its function
]

