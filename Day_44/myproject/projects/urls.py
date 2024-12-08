from . import views

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

app_name = 'projects'

urlpatterns = [

    path('', views.projects_list, name='list'),
    path('<int:id>/',views.project_page, name='page'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)