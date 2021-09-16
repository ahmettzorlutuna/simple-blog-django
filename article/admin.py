from django.contrib import admin

from .models import Article, Comment  #oluşturduğmuz uygulamayı import ettik. yani kayıt ettik
# Register your models here.

admin.site.register(Comment) # comment modelimizi kayıt ettik burada

@admin.register(Article) #kayıt ettik
class ArticleAdmin(admin.ModelAdmin): #admin panelini özelleştireceğimiz class ı oluşturduk

    list_display = ["title","author","created_date"]

    list_display_links = ["title","created_date"]  #makalelerimizin olduğu kısımda diğer özelliklere de link verdik

    search_fields = ["title"]  #title'a göre arama yapma özelliğimizi ekledik

    list_filter = ["created_date"] #makalelerimizi created date e göre sıralana

    
    class Meta: # kayıt ettiğimiz modelimizle özelliştirdiğimiz admin panelini birleştirdik
        model = Article
        
