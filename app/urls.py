from django.urls import path
from .views.auth import login, register, profile, logout
from .views.battle import get, winner


urlpatterns = [
    
    path('',profile.ProfileView,name='profile'),
    path('battle/<str:battleuuid>/',get.BattleView,name='battle'),
    path('battle/<str:battleuuid>/winner/',winner.WinnerView,name='winner'),

    path('logout/',logout.LogoutView,name='logout'),
    path('login/',login.LoginView,name='login'),
    path('register/',register.RegisterView,name='register'),
    
]