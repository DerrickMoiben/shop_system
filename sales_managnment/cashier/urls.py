
from django.urls import path
from cashier import views

urlpatterns = [
    path('sing-up/', views.sign_up, name='sign-up'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('record-sale/', views.record_sale, name='record-sale'),
]