from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=10, unique=True,
                                verbose_name='姓名')
    password = models.CharField(max_length=255, verbose_name='密码')
    icon = models.ImageField(upload_to='upload', null=True, verbose_name='头像')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    class Meta:
        db_table = 'users'


class Category(models.Model):
    category = models.CharField(max_length=10, verbose_name='栏目',null=True)
    nick_name = models.CharField(max_length=20, verbose_name='别名', null=True)
    fid = models.CharField(max_length=20,verbose_name='父节点', null=True)
    keywords = models.CharField(max_length=20, verbose_name='关键字', null=True)
    describe = models.CharField(max_length=100, verbose_name='描述', null=True)

    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=10, verbose_name='标题',null=True)
    content = models.TextField(null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间',null=True)
    key_words = models.CharField(max_length=10, verbose_name='关键字', null=True)
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE,
                          related_name='art')

    class Meta:
        db_table = 'article'


class Resume(models.Model):
    username = models.CharField(max_length=10, unique=True,
                                verbose_name='姓名')
    icon = models.ImageField(upload_to='upload', null=True, verbose_name='头像')
    resume = models.CharField(max_length=1000,null=True,verbose_name='个人简介')

    class Meta:
        db_table = 'resume'

