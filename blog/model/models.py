# models.py
from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=64, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='密码')
    class Meta:
        db_table = 'python_admin'

class Category(models.Model):
    category_name = models.CharField(max_length=32, verbose_name='分类名称')
    sort = models.IntegerField(default=0,verbose_name='排序')
    status = models.IntegerField(default=0,verbose_name='状态')
    class Meta:
        db_table = 'python_category'

class Article(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='文章',on_delete=models.CASCADE)
    title = models.CharField(max_length=32, verbose_name='标题')
    summary = models.CharField(max_length=128, verbose_name='摘要')
    content = models.TextField(null=True,verbose_name='内容')
    time = models.IntegerField(default=0,verbose_name='时间')
    image = models.CharField(max_length=128, verbose_name='图片路径')
    # category_id = models.IntegerField(default=0,verbose_name='分类id')
    click_number = models.IntegerField(default=0,verbose_name='点击量')
    status = models.CharField(max_length=32, verbose_name='状态，1：正常，0：隐藏')
    class Meta:
        db_table = 'python_article'

class ArticleTag(models.Model):
    article_id = models.IntegerField(default=0,verbose_name='文章id')
    tag_id = models.IntegerField(default=0,verbose_name='标签id')
    class Meta:
        db_table = 'python_article_tag'

class Tag(models.Model):
    tag_name = models.CharField(max_length=32, verbose_name='标签名称')
    class Meta:
        db_table = 'python_tag'
