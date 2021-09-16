"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:  
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings  
from django.conf.urls.static import static


from article import views #views içinde render ettiğimiz sayfaların url lerine ulaşmak için import views dedik
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name = "index"),  #name değeri ile şuan da belirlediğimiz gitmek istediğimiz url ye isim verdik. Buda bizim ileride redirect urlfor yapmamızı sağlayacak
    path('about/', views.about,name = "about"),
    #path('detail/<int:id>',views.detail,name = "detail"),  #detail/<int:id> şeklinde dinamik url mizi tanımladık
    path('articles/',include("article.urls")),    #<-----burada olduğu gibi bazı durumlarda sitemizdeki url kısmına yazdığımız url sadece tek bir kalıp halinde olabilir. 
                                                                    #Örn: articles/update - articles/add - articles/delete bu şekilde olduğu zamana articlesdan 
                                                                    #sonra gelen urlimizi bu urls dosyasına değil de sadece articcles için çağıracağımız urlleri 
                                                                    #burada include edeceğimizbaşka bir dosyaya yazacağız.    
    path('user/',include("user.urls"))  #burada da yukarıdaki işlemin aynısı. Örn: user/register or user/loginUser  or logoutUser
]

if settings.DEBUG:    #media klasörümüze erişim için 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
