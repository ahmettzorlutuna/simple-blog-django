from django import forms
from django.forms.widgets import RadioSelect #wtf formuna gerek kalmadı bu djangonun kendi from yapısı

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı")
    password = forms.CharField(max_length=20, label="Parola", widget=forms.PasswordInput)

class RegisterForm(forms.Form):   #forms.form clasındam formu türettik
    username = forms.CharField(max_length=50 , label="Kullanıcı Adı")  #burada form alanlarımızı oluşturuyoruz. register form sayfasında bu kısım input type olarak gözükecek
    password = forms.CharField(max_length=20 , label="Parola" , widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20 , label="Parolayı Doğrulayın" , widget=forms.PasswordInput)

    def clean(self):  #formu validate etmek için
        username = self.cleaned_data.get("username")  #Burada formumuzdaki bilgileri aldık. Çünkü aşağüıda confirm kontrolünü yapacazğız
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:  #password ve confirm alanının dolu olup olmadığı ve password ve confirm in aynı olup olmadığı
            raise forms.ValidationError("Parolalar eşleşmiyor")

        values = {     #if durumu gerçekleşmezse burada bir sonraki sayfada dönmek için form bilgilerimizi aldık
            "username" : username,  
            "password" : password,
        }
        return values