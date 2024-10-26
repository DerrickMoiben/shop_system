
from django.urls import path
from cashier import views

urlpatterns = [
    path('cashier-dashboard/', views.cashier_dashboard, name='cashier-dashboard'),
    path('cashier-sing-up/', views.cashier_sing_up, name='cashier-sign-up'),
    path('cashier-login/', views.cashier_login, name='cashier-login'),
    path('stock_add/', views.stock_add, name='stock_add'),
    path('sales-summary/', views.sales_summary, name='sales-summary'),
]