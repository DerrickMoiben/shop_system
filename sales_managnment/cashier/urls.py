
from django.urls import path
from cashier import views

urlpatterns = [
    path('cashier-sing-up/', views.cashier_sing_up, name='cashier-sing-up'),
    path('cashier-login/', views.cashier_login, name='cashier-login'),
]