from article import views
from django.contrib import admin
from django.urls import path
from . import views
app_name = "article"  #ileride redirect işlemi yaparken uygulamayı ve o uygulamaya ait url yi belirtmek için uygulamaya isim verdik

urlpatterns = [
    path('dashboard/',views.dashboard,name="dashboard"),  #views.dashboard çağırdığımız fonksiyon
    path('addarticle/',views.addArticle,name="addarticle"),  #views.dashboard çağırdığımız fonksiyon
    path('article/<int:id>',views.detail,name="detail"),  #dashboard da seçilen makaleye göre dinamik url yapısı
    path('update/<int:id>',views.updateArticle,name="update"),  #makale güncelleme
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.addComment,name="comment"),
]