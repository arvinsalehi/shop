from django.urls import path
from .views import Login_user, Register_user, log_out, user_panel, user_edit_panel

app_name = "login_register"

urlpatterns = [
    path('login', Login_user, name='Login'),
    path('register', Register_user, name='Register'),
    path('log-out', log_out, name='Logout'),
    path('user', user_panel, name="user"),
    path('user/edit', user_edit_panel, name="user-edit"),
]
