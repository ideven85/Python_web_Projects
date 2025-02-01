from django.urls import path,include
from django.contrib.auth import views as auth_views
from core.user import views

urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutView.as_view(),name='logout')
    path('', include('django.contrib.auth.urls')), #todo Better to build own authentication stuff,
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]