from django.shortcuts import render 
from .forms import CustomLoginForm , AdminAddUserForm
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from allauth.account.views import LoginView , LogoutView 
from django.urls import reverse_lazy
# Create your views here.

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('userList')
    
    
class CustomLogoutView(LogoutView):
    pass



class AdminAddUserView(UserPassesTestMixin,CreateView):
    template_name = 'auth/adduser.html'
    form_class = AdminAddUserForm
    success_url = reverse_lazy('userList')
    
    def test_func(self) -> bool | None:
        return self.request.user.is_staff
    
    
    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['custom_message'] = 'User has been added successfully!'
        return response

    def get_success_url(self):
        return reverse_lazy('userList')