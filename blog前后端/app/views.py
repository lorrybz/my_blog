import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# def index(request):
#     if request.method == 'GET':
#         print('index views')
#         1/0
#         return HttpResponse('我是index方法')
        # 1/0
        # return render(request, 'index.html')

#
# def index(request):
#     print('index views')
#
#     def index_render():
#         return render(request, 'index.html')
#
#     rep = HttpResponse()
#     rep.render = index_render
#     return rep


def index(request):
    """
    index方法中添加记录日志
    """
    if request.method == 'GET':
        logger.info('index方法')
        return HttpResponse('我是首页，我需要有修改用户名的权限才能访问')