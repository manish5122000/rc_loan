from django.urls import path
from django.contrib.auth import views as auth_views
from adminss import views
from .forms import LoginForm,  MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm



urlpatterns = [
    path('',views.home, name='home'),


    #Authentication
    path('registerpg/', views.RegistrationPage,name='rpage'),

    path('admin-registration/', views.AdminRegistration, name='adminregistration'),
    #login
    path('accounts/login/',auth_views.LoginView.as_view(template_name='adminss/login.html',authentication_form=LoginForm),name='login'),
     # 3-Logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    #Password change
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='adminss/passwordchange.html',
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='adminss/passwordchangedone.html'),name='passwordchangedone'),
    # 5-password reset
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='adminss/password_reset.html',
        form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='adminss/password_reset_done.html')
        ,name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='adminss/password_reset_confirm.html'
        ,form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='adminss/password_reset_complete.html')
        ,name='password_reset_complete'),
]