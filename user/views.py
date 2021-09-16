from django import forms
from django.shortcuts import render,redirect
from .forms import LoginForm, RegisterForm  #.forms şuanki forms klasöründen
from django.contrib import messages #message frameworkünü dahil ettik
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout


# Create your views here.

#UYARI UYARI : eğer kayıt olma aşamasında kullanıcı adı daha önceden kayıt edilmişse hata mesajı verilecek


def register(request):

    form = RegisterForm(request.POST or None) #post request olduğunda formumuz gelen bilgilerle doldurulacak ve is lavid olacak ve kayıt işlemi gerçekleştirilecek. is valid olmazsa context kısmı çalışacak
    if form.is_valid(): #Biz bu fonksiyonu çağırdığımızda yazdığımız clena fonksiyonu otomatik olarak çağırılıyor ve içindeki değerler dönüyor. form.is_valid true dönerde clean fonksiyonunun if komutu çalışıyor
        username = form.cleaned_data.get("username") #form alanlarımıza girilen değerleri aldıks
        password = form.cleaned_data.get("password")
        
        newUser = User(username = username) #girilen bilgilerle newUser objemizi oluşturduk
        newUser.set_password(password)
        
        newUser.save() #newUser ımızı veritabanına kayıt ettik
        login(request,newUser) #kayıt edilen newUsermızı aynı zamanda sisteme login yapmış olduk djangonun kendi yapısıyla
        messages.success(request, "Başarıyla kayıt oldunuz.")
        
        return redirect("index") #index e gidelin urlmizin ismini(index) redirect işlemi olarak gönderdik
    context = {    #formumuzu register.html göndermek için form anahtar kelimesiyle oluşturduk contexti
            "form" : form
        }
    return render(request , "register.html",context)
    

def loginUser(request):

    form = LoginForm(request.POST or None)
    
    context = {
        "form" : form
    }
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        
        user = authenticate(username = username , password = password)  #authenticate ile formdan aldığımız username ve password bilgilerini databasede olup olmadığını kontrol edeceğiz.
        
        if user is None:  #eğer kullanıcı yoksa
            messages.info(request, "Kullanıcı adı veya parola hatalı")
            return render(request,"login.html",context)   #forms kısmında oluşturduğumuz loginform u form adlı değişkene atadık. ardından context (içerik) olarak da form u içine gönderip html de gösterdik
        
        messages.success(request,"Başarıyla giriş yaptınız")
        login(request,user) #kullanıcıyı giriş yaptırdık
        return redirect("index")
    return render(request, "login.html" ,context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla çıkış yaptınız")
    return redirect("index")

