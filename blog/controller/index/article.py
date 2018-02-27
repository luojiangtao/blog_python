from django.http import HttpResponse
from django.shortcuts import render
from blog import tool

def list(request):
    id = request.GET['id']
    article_list=tool.executeQuery(sql='SELECT * FROM python_article where category_id=%s',param=[id])
    # article_list=tool.executeQuery(sql=f"SELECT * FROM python_article where category_id={id}")
    category_list=tool.executeQuery(sql="SELECT * FROM python_category")
    for key,value in enumerate(article_list):
        # print(key,value)
        sql=f"SELECT category_name FROM python_category where id={value['category_id']}"
        category = tool.executeQuery(sql)
        # print(category)
        article_list[key]["category_name"] = category[0]['category_name']

    return render(request, 'index/list.html', locals())
def detail(request):
    id = request.GET['id']
    article_list=tool.executeQuery(sql='SELECT * FROM python_article where id=%s',param=[id])

    for key,value in enumerate(article_list):
        # print(key,value)
        sql=f"SELECT category_name FROM python_category where id={value['category_id']}"
        category = tool.executeQuery(sql)
        # print(category)
        article_list[key]["category_name"] = category[0]['category_name']
    article=article_list[0]

    return render(request, 'index/detail.html', locals())