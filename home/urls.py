from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home', views.home_page, name='home'),
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('logout_user', views.logout_user, name="logout"),
    path('profile', views.profile, name='profile'),

]