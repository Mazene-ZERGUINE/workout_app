from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name="home"),
    path('', include('base.urls'))
]


urlpatterns += staticfiles_urlpatterns()
