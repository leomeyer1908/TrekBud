# travel/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path('select-region/', views.select_region, name='select_region'),
	path('travel/', include('travel.urls')),
]

