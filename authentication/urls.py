from django.urls import path , include
from .views import CustomLoginView , CustomLogoutView , AdminAddUserView
urlpatterns = [
    path('login',CustomLoginView.as_view(),name='login'),
    path('logout',CustomLogoutView.as_view(),name='logout'),
    path('adduser',AdminAddUserView.as_view(),name='adduser'),
    path('adduser',AdminAddUserView.as_view(),name='account_signup'),
    
]
