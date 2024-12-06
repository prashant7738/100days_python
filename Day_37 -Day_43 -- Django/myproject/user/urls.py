from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_view, name='register'),  # Ensure correct endpoint
    path('login/', views.login_view, name='login'),  
    path('logout/', views.logout_view, name='logout'),  
]
