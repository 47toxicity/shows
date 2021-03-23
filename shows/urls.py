from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'shows-home'),
    path('about/', views.about, name = 'shows-about'),
]