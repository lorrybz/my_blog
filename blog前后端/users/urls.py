
from django.urls import path

from users import views

urlpatterns = [
    # 注册
    path('register/', views.register, name='register'),
    # 登录
    path('login/', views.login, name='login'),
    # 首页
    path('index/', views.index, name='index'),
    # 注销
    path('logout/', views.logout, name='logout'),
    # 编辑文章
    path('edit_article/<int:id>/', views.edit_article, name='edit_article'),
    # 文章列表
    path('article/', views.article, name='article'),
    path('category/', views.category, name='category'),
    path('add_article/', views.add_article, name='add_article'),
    path('del_article/<int:id>/', views.del_article, name='del_article'),
    path('add_category/', views.add_category, name='add_category'),
    path('del_category/<int:id>/', views.del_category, name='del_category'),
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path('add_resueme/',views.add_resueme,name='add_resueme')
]

