from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('create_journey', views.createJourney, name='create_journey'),
    path('update_journey/<str:pk>/', views.updateJourney, name='update_journey'),
    path('delete_journey/<str:pk>/', views.deleteJourney, name='delete_journey'),
]
