from django.urls import path
from manager import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('manager-sing-up/', views.manager_sing_up, name='manager-sign-up'),
    path('manager-login/', views.manager_login, name='manager-login'),
    path('new-staff/', views.new_staff, name='new-staff'),
    path('all-stock/', views.all_stock, name='all-stock'),
    path('edit-stock/<int:stock_id>/', views.edit_stock, name='edit-stock'),
]