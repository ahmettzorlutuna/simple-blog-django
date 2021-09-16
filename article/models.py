from django.db import models
from ckeditor.fields import RichTextField  #ckeditörü dahil ettik

# Create your models here.
# Article uygulamamıza ait modellerimizi oluşturacağımız yer.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Yazar")  #bu alanımızı hazırda bulunan user tablosundan alıyoruz (Foreign key). 
    title = models.CharField(max_length= 50,verbose_name="Başlık")                            #hazırda bulunan user tablosunu göstermiş oluyoruz.yani girilen kullanıcı databaseden silindiğinde o kullanıcıya ait tüm makaleler ve veriler silinecek(on_delete = models.CASCADE).
    content = RichTextField()  #dahil ettiğimiz ckeditörü Article appimizde content kısmını richtextfield olarak tanımladık.
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")  #auto_now_add=True o anki tarihi zamanı otomatik atama
    article_image = models.FileField(blank=True,null=True,verbose_name="Makaleye fotoğraf ekleyin")  #makaleye resim veya dosya ekleme kısmı
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date'] #en son yüklenene göre 
class Comment(models.Model):     #comment modelimizi oluşturduk
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Makale",related_name="comments")  #foreign key yardımı ile article modelimiz ile ilişkilendirdik ve ilerdie makaleleri alırken yorumunu da almak için article.comments diyerek alıcaz 
    comment_author = models.CharField(max_length= 50 ,verbose_name="İsim",null=True)
    comment_content = models.CharField(max_length= 200 ,verbose_name="Yorum",null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Yazar..: {} Makalesi..: {}".format(self.comment_author, self.comment_content)

    class Meta:
        ordering = ['-comment_date'] #en son yüklenene göre 
    