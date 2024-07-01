from django.urls import path
from manager import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('manager-sing-up/', views.manager_sing_up, name='manager-sign-up'),
    path('manager-login/', views.manager_login, name='manager-login'),
    
]