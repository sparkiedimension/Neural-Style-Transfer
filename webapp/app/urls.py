from django.urls import path
from . import views

urlpatterns = [
    path('logout/', views.auth_logout),
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('dashboard/', views.DashboardView.as_view())
]