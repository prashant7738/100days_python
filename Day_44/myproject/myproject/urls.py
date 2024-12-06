from . import views

from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('about/',views.about ),
    path('projects/' , include('projects.urls'))
]
