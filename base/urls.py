from django.urls import path 
from . import views 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register, name="register"),
    path('profile' , views.profile , name="profile"),
    path('logout' , views.user_logout),
    path("add_new_exercice" , views.add_exercice, name="new_exercice"),
    path("delete_exercice/<str:exo>", views.delete_exercice) , 
    path('edit_exercice/<str:edited>' , views.edit_exercice)
]

urlpatterns += staticfiles_urlpatterns()
