from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordChangeView,
    PasswordChangeDoneView,
)

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/',
         LoginView.as_view(template_name='users/login.html'),
         name='login'
         ),
    path('pass_reset/', PasswordResetView.as_view(
         template_name='users/password_reset_form.html'),
         name='pass_reset'
         ),
    path('pass_reset_confirm/', PasswordResetConfirmView.as_view(
         template_name='users/password_reset_confirm.html'),
         name='pass_reset_confirm'
         ),
    path('pass_reset_done/', PasswordResetDoneView.as_view(
         template_name='users/password_reset_done.html'),
         name='pass_reset_done'
         ),
    path('pass_change/', PasswordChangeView.as_view(
         template_name='users/password_change_form.html'),
         name='pass_change'
         ),
    path('pass_change_done/', PasswordChangeDoneView.as_view(
         template_name='users/password_change_done.html'),
         name='pass_change_done'
         ),
]
