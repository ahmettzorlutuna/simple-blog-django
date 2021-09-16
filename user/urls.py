from django.contrib import admin
from django.urls import path
from . import views
app_name = "user"  #ileride redirect işlemi yaparken uygulamayı ve o uygulamaya ait url yi belirtmek için uygulamaya isim verdik

urlpatterns = [
    path('register/',views.register,name="register"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name="logout"),
    
]