from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registration, name='registration'),
	path('confirm/<str:uidb64>/<str:token>/', views.confirm_email, name='confirm_email'),
]
