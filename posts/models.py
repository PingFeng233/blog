from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    content = models.TextField(verbose_name='正文')
    category = models.CharField(verbose_name='标签', max_length=15)
    created_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    active = models.BooleanField(verbose_name='是否激活', default=True)
    cover = models.ImageField(verbose_name='封面', default='default.jpg')
    view_nums = models.IntegerField(verbose_name='访问量')
    comment = models.TextField(verbose_name='评论')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
