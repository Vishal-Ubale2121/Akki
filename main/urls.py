from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main_home'),  # Redirects to portfolio:home
    path('about/', views.about, name='main_about'),  # Redirects to portfolio:about
]
