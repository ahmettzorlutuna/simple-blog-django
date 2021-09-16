#addarticle da makale ekleme formu oluşturma dosyası

from django import forms
from .models import Article #article modelimizi modelform ile ilişkilendirmek için article modelimizi dahil ettik

class ArticleForm(forms.ModelForm):  #bizim zaten hazırladığımız bir article modelimiz bulunmakta. ve biz o modele göre bu formumuuzu oluşturacağımız için djangonun model form yapısını kullanacağız.
    class Meta:
        model = Article # modeli kendi article modelimizle ilişkilendirdik
        fields = ["title","content","article_image"]  #oluşturmak istediğimiz inputları belirledik
