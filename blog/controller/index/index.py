from django.http import HttpResponse
from django.shortcuts import render
from blog.model.models import Category
from blog.model.models import Article
from pprint import pprint
from django.db import connection

def index(request):
    # category_list = Category.objects.all()
    # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # # Test.objects.order_by('name')[0:2]
    # article_list = Article.objects.order_by("id")[0:2]
    # pprint(article_list.ca)
    # return render(request, 'index/index.html', locals())

    cursor = connection.cursor()

    # Data retrieval operation. This doesn't dirty the transaction,
    # so no call to set_dirty() is required.

    cursor.execute("SELECT * FROM python_category")
    category_list = dictfetchall(cursor)

    cursor.execute("SELECT * FROM python_article")
    article_list = dictfetchall(cursor)
    # print(article_list)
    # for key,value in article_list.items():
    #     print(key,value)

    # category_list = cursor.fetchall()
    # category_list = list(category_list)
    # print(article_list)
    return render(request, 'index/index.html', locals())

def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    print(desc)
    retult =  [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]
    return retult
