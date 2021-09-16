import article
from article.models import Article
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404,reverse
from .forms import ArticleForm
from .models import Article,Comment
from django.contrib import messages #message frameworkünü dahil ettik
from django.contrib.auth.decorators import login_required
# Create your views here.
# url çağırıldığında yazılacak fonksiyonlar
def articles(request):
    keyword = request.GET.get("keyword") # arama çubuğu kısmına yazılan keyword değerini get request sonrası aldık
    
    if keyword:  # arama işlemi yapıldı mı ?
        articles = Article.objects.filter(title__contains = keyword)  # arama işlemi sonrası get requestten aldığımız keyword değeri makalelerimizin hernagi birinde bulnuyor mu title contains ile baktık
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all() #tüm article lerimizi liste halinde aldık 
    return render(request,"articles.html",{"articles":articles}) #html sayfamıza articles değişkenimizi articles olarak gönderdik
    
def index(request):    #index sayfamız için request değerini içine gönderdiğimiz fonksiyon. 
    
    context = {   #index.html için context içerikli sözlük
        "number1" : 10,
        "number2" : 20
    }

    return render(request,"index.html",context) #burada içerik yani context olarak templates sayfalarımızdan index.html context şeklinde bir sözlük yapısı gönderdik
    

def about(request):
    return render(request,"about.html")

@login_required(login_url = "user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)  #sadece giriş yapan userın makalesi
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html",context)

@login_required(login_url = "user:login")
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None) #article form objemizi oluşturduk

    if form.is_valid():
        
        article = form.save(commit=False)   #commit false sebebi şu biz formu save form diyoruz ama kayıt etmeden önce user id belirtmiyoruz 
                                            #ve hata alıyruz. o yüzden kendisi kaydetmeyecek ve biz user id belirttikten sonra biz kaydettireceğiz
        article.author = request.user  #formdan aldığımız bilgilerle döndüğümüz article objesine authoru belirrtik ve 
        article.save()  #kayıt işlemini gerçekleştirdik
        messages.success(request,"Makale başarıyla oluşturuldu")
        return redirect("article:dashboard")
    return render(request, "addarticle.html" ,{"form":form})  #context olarak formumuzu gönderdik

def detail(request,id):
    #article = Article.objects.filter(id = id).first()   #seçilen id ye ait article objemizi döndük. dönen listeyi first diyerek hemen bastırdık
    article = get_object_or_404(Article , id=id)  #çektiğimiz model ve sorgumuz
    comments = article.comments.all() #article ın ilişkili olsuğu tüm yorumları aldık
    return render(request,"detail.html",{"article":article,"comments":comments}) #dönen objemizi detail.html sayfasına gönderdik ve render ettik

@login_required(login_url = "user:login")
def updateArticle(request,id):

    article = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None,request.FILES or None,instance=article) #instance yeni eklediğimiz bilgileri forma göndermek için article objemizi içine gönderdik
    if form.is_valid():
        article = form.save(commit=False)   #commit false sebebi şu biz formu save form diyoruz ama kayıt etmeden önce user id belirtmiyoruz 
                                            #ve hata alıyruz. o yüzden kendisi kaydetmeyecek ve biz user id belirttikten sonra biz kaydettireceğiz
        article.author = request.user  #formdan aldığımız bilgilerle döndüğümüz article objesine authoru belirrtik ve 
        article.save()  #kayıt işlemini gerçekleştirdik
        messages.success(request,"Makale başarıyla güncellendi")
        return redirect("article:dashboard")
    
    return render(request,"update.html",{"form":form}) # get request veya form invalid değilse formumuzu sayfaya gönderdik

@login_required(login_url = "user:login") 
def deleteArticle(request,id):

    article = get_object_or_404(Article,id = id)  #article modelinden article objemizi oluşturduk
    
    article.delete()
    
    messages.success(request,"Makale Başarıyla Silindi")
    
    return redirect("article:dashboard") #articleın içindeki dashboard a git

def addComment(request,id):
    article = get_object_or_404(Article,id = id)  #yorumu hangi makaleye ekleyeceğmiz için article objesini oluştuduk ve id yi içine verdik
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")  #posttan gelen bilgileri aldık
        comment_content = request.POST.get("comment_content") #posttan gelen bilgileri aldık
        
        newComment = Comment(comment_author  = comment_author, comment_content = comment_content) #aldığımız bilgiler ile yeni yorum adlı objemizi oluşturudk bunu göstereceğiz
        
        newComment.article = article # yeni yorumumuzun hangi article a ait olduğunu bildirmek için 
        
        newComment.save()
        
        
    return redirect(reverse("article:detail",kwargs={"id":id}))  #/articles/article/" + str(id) yani /articles/detail/14  
#def detail(request,id):  #fonksiyonumuzu yazdık ilk olarak request göndermemiz lazım parametre olarak gönderdilk ynında da urls kısmında tanımladığımız dinamik url id sini yazdık
    #return HttpResponse("Detail:" + str(id))  #id yi stringe çevirdik response döndürmek için. çünkü urls kısmında id yi int olarak gönderdik