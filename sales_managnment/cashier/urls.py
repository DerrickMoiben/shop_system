
from django.urls import path
from cashier import views

urlpatterns = [
    path('cashier-sing-up/', views.cashier_sing_up, name='cashier-sign-up'),
    path('cashier-login/', views.cashier_login, name='cashier-login'),
    path('cashier-dashboard/', views.cashier_dashboard, name='cashier-dashboard'),
    path('add-sale-item/', views.add_sale_item, name='add_sale_item'),
]