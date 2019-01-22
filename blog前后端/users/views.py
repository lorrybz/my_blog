
from datetime import timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from users.models import Users, Article, Category, Resume


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        # all()校验参数，如果列表中元素为空，则返回False
        if not all([username, password, password2]):
            msg = '请填写完整的参数'
            return render(request, 'register.html', {'msg': msg})
        if password != password2:
            msg = '密码不一致,请重新填写'
            return render(request, 'register.html', {'msg': msg})
        Users.objects.create(username=username,
                             password=make_password(password))
        # 注册成功跳转到登录方法
        return HttpResponseRedirect(reverse('users:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        # 使用cookie+session形式实现登录
        username = request.POST.get('username')
        password = request.POST.get('password')
        # all()校验参数，如果列表中元素为空，则返回False
        if not all([username, password]):
            msg = '请填写完整的参数'
            return render(request, 'login.html', {'msg': msg})
        # 校验是否能通过username和pasword找到user对象
        user = Users.objects.filter(username=username).first()
        if user:
            # 校验密码
            if not check_password(password, user.password):
                msg = '密码错误'
                return render(request, 'login.html', {'msg': msg})
            else:
                # 向cookie中设置，向user_ticket表中设置
                request.session['user_id'] = user.id
                # 设置session数据在4天后过期过期时间
                request.session.set_expiry(timedelta(days=4))
                return HttpResponseRedirect(reverse('users:index'))
        else:
            msg = '用户名错误'
            return render(request, 'login.html', {'msg': msg})


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def logout(request):
    if request.method == 'GET':
        # 注销，删除session和cookie
        request.session.flush()
        # 获取session_key并实现删除,删除服务端
        # session_key = request.session.session_key
        # request.session.delete(session_key)
        return HttpResponseRedirect(reverse('users:login'))


def edit_article(request,id):
    """
    文章编辑方法
    """
    if request.method == 'GET':
        article = Article.objects.filter(pk=id).first()
        aaa = Category.objects.all()
        title = article.title
        id = article.category_id
        category = article.category.category
        key_words = article.key_words
        content = article.content
        result = [title,category,key_words,content,id]
        return render(request, 'edit.html',{'result':result,'aaa':aaa})
    if request.method == 'POST':
        # 获取文章的标题和内容
        title = request.POST.get('title')
        category_id = request.POST.get('category')
        content = request.POST.get('content')
        key_words = request.POST.get('keywords')

        # 使用all()方法进行判断，如果文章标题和内容任何一个参数没有填写，则返回错误信息
        if not all([title, content]):
            msg = '请填写完整的参数'
            return render(request, 'edit.html', {'msg': msg})

        # 修改文章
        article = Article.objects.filter(pk=id).first()
        article.title=title
        article.category_id=category_id
        article.content=content
        article.key_words=key_words
        article.save()
        # 创建文章成功后，跳转到文章列表页面
        return HttpResponseRedirect(reverse('users:article'))


def article(request):
    """
    文章展示方法
    """
    if request.method == 'GET':
        page = int(request.GET.get('page',1))
        # 第一种使用切片实现分页
        # http://127.0.0.1:8080/app/all_stu/?page=1
        # stus = Student.objects.all()[((page-1)*3):(page*3)]
        # 第二种使用paginator实现
        result3 = []
        articles = Article.objects.all()
        i = 1
        for article in articles:
            title = article.title
            category = article.category.category
            key_words = article.key_words
            content = article.content
            create_time = article.create_time
            id = article.id
            result2=[title,category,key_words,content,create_time,id]
            result3.append(result2)
        pg = Paginator(result3,5)
        result3 = pg.page(page)
        return render(request, 'article.html',{'result3':result3})


def category(request):
    """
    栏目展示方法
    """
    if request.method == 'GET':
        cat = Category.objects.all()
        results = []
        for categorys in cat:
            category = categorys.category
            nick_name = categorys.nick_name
            total = Article.objects.filter(category_id=categorys.id).count()
            id = categorys.id
            aaa = [category,nick_name,total,id]
            results.append(aaa)
        return render(request, 'category.html',{'results':results})


def add_article(request):
    if request.method == 'GET':
        category = Category.objects.all()
        return render(request,'add_article.html',{'category':category})
    if request.method == 'POST':
        # 1获取数据

        title = request.POST.get('title')
        category = request.POST.get('category')
        content = request.POST.get('content')
        key_words = request.POST.get('keywords')
        Article.objects.create(title=title,
                               category_id=category,
                               content=content,
                               key_words=key_words,)
        return HttpResponseRedirect(reverse('users:article'))


def del_article(request,id):
    if request.method == 'GET':
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('users:article'))


def add_category(request):
    if request.method == 'GET':
        return render(request, 'category.html',)
    if request.method == 'POST':
        category = request.POST.get('name')
        nick_name = request.POST.get('alias')
        fid = request.POST.get('fid')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')

        Category.objects.create(category=category,
                                nick_name=nick_name,
                                fid=fid,
                                keywords=keywords,
                                describe=describe)
        return HttpResponseRedirect(reverse('users:category'))


def del_category(request,id):
    if  request.method == "GET":
        articles = Article.objects.filter(category_id=id)
        if articles:
            articles.delete()
        Category.objects.filter(id=id).delete()
        return HttpResponseRedirect(reverse('users:category'))

def edit_category(request,id):
    if  request.method == "GET":
        categorys = []
        cat = Category.objects.filter(id=id).first()
        cats = Category.objects.all()
        for i in cats:
            category = i.category
            categorys.append(category)
        return render(request,'edit_category.html', {'categorys': categorys,'cat':cat})

    if request.method == 'POST':
        category = request.POST.get('name')
        nick_name = request.POST.get('alias')
        fid = request.POST.get('fid')
        keywords = request.POST.get('keywords')
        describe = request.POST.get('describe')

        Category.objects.create(category=category,
                                nick_name=nick_name,
                                fid=fid,
                                keywords=keywords,
                                describe=describe)
        return HttpResponseRedirect(reverse('users:category'))


def add_resueme(request):
    if request.method == 'GET':
        resumes = Resume.objects.first()
        return render(request,'resume.html',{'resume':resumes})

    if request.method == 'POST':
        # 1获取数据
        resumes = Resume.objects.first()
        username = request.POST.get('username')
        icon = request.FILES.get('icon')
        resume = request.POST.get('resume')

        resumes.username=username
        resumes.icon=icon
        resumes.resume=resume
        resumes.save()

        # 2.保存
        # 3.跳转页面
        return HttpResponseRedirect(reverse('front:index'))