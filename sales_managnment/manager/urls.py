from django.urls import path
from manager import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
]