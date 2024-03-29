from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('create_journey', views.createJourney, name='create_journey'),
    path('update_journey/<str:pk>/', views.updateJourney, name='update_journey'),
    path('delete_journey/<str:pk>/', views.deleteJourney, name='delete_journey'),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
     name='reset_password'),

    path('password_reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'), 
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
     name='password_reset_confirm'),

    path('reset/done/', 
        auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), 
        name='password_reset_complete'),
]
