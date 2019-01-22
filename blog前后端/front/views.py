from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from users.models import Resume, Category, Article


def index(request):
    resume = Resume.objects.first()
    cat = Category.objects.all()
    results = []
    for categorys in cat:
        category = categorys.category
        total = Article.objects.filter(category_id=categorys.id).count()
        id = categorys.id
        aaa = [category,total,id]
        results.append(aaa)
    articles = Article.objects.all()
    first = articles.first()
    page = int(request.GET.get('page', 1))
    pg = Paginator(articles, 3)
    articles = pg.page(page)
    return render(request,'index_lorry.html',{'resume':resume,
                                              'results':results,
                                              'articles':articles,
                                              'first':first},)


def list(request):
    resume = Resume.objects.first()
    cat = Category.objects.all()
    results = []
    for categorys in cat:
        category = categorys.category
        total = Article.objects.filter(category_id=categorys.id).count()
        id = categorys.id
        aaa = [category,total,id]
        results.append(aaa)
    articles = Article.objects.all()
    articles1 = articles
    first = articles.first()
    page = int(request.GET.get('page', 1))
    pg = Paginator(articles, 5)
    articles = pg.page(page)
    return render(request,'list_lorry.html',{'resume':resume,
                                              'results':results,
                                              'articles':articles,
                                              'articles1': articles1,
                                              'first':first},)




def infopic(request,id):
    article = Article.objects.filter(id=id).first()
    resume = Resume.objects.first()
    cat = Category.objects.all()
    results=[]
    for categorys in cat:
        category = categorys.category
        total = Article.objects.filter(category_id=categorys.id).count()
        id = categorys.id
        aaa = [category,total,id]
        results.append(aaa)

    return render(request, 'infopic_lorry.html', {'resume': resume,
                                                    'results': results,
                                                    'article':article
                                                    })


def about(request):
    results = []
    cat = Category.objects.all()
    for categorys in cat:
        category = categorys.category
        total = Article.objects.filter(category_id=categorys.id).count()
        aaa = [category,total]
        results.append(aaa)

    return render(request, 'about_lorry.html',{'results':results})










