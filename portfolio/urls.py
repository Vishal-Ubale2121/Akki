from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),

    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    #path("admin-logout/", views.admin_logout, name="admin_login"),

    path('portfolio/', views.portfolio, name='portfolio'),
    path('photo/<int:photo_id>/', views.photo_detail, name='photo_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('Admin/', views.admin_login, name='admin'),
    path('services/', views.services, name='services'),
]
