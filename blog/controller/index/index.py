from django.http import HttpResponse
from django.shortcuts import render
from blog.model.models import Category
from blog.model.models import Article
from blog import tool

def index(request):
    # category_list = Category.objects.all()
    # # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    # # Test.objects.order_by('name')[0:2]
    # article_list = Article.objects.order_by("id")[0:2]
    # pprint(article_list.ca)
    # return render(request, 'index/index.html', locals())

    # Data retrieval operation. This doesn't dirty the transaction,
    # so no call to set_dirty() is required.

    article_list=tool.executeQuery("SELECT * FROM python_article")
    category_list=tool.executeQuery("SELECT * FROM python_category")
    for key,value in enumerate(article_list):
        # print(key,value)
        sql=f"SELECT category_name FROM python_category where id={value['category_id']}"
        category = tool.executeQuery(sql)
        # print(category)
        article_list[key]["category_name"] = category[0]['category_name']
    # for k,v in category_list.items():
    #     print(k,v['category_name'])
    # print('category_list',category_list)
    print('article_list',article_list)

    # for key,value in category_list.items():
    #     print(key,value)

    # category_list = cursor.fetchall()
    # category_list = list(category_list)
    # print(article_list)
    return render(request, 'index/index.html', locals())
