from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='标题', max_length=50)
    content = models.TextField(verbose_name='正文')
    created_time = models.DateField(verbose_name='创建时间', auto_now_add=True)
    active = models.BooleanField(verbose_name='是否激活', default=True)
    cover = models.ImageField(verbose_name='封面', default='default.jpg',
                              upload_to='avatar/%Y/%m/%d')
    view_nums = models.IntegerField(verbose_name='访问量',default=0)
    comment = models.TextField(verbose_name='评论')
    labels = models.ManyToManyField('Labels', verbose_name='标签')
    category = models.ForeignKey('Category', verbose_name='类别')

    def increase_view(self):
        self.view_nums += 1
        self.save(update_fields=['view_nums'])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'


class Category(models.Model):
    name = models.CharField(verbose_name='类别', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'


class Labels(models.Model):
    name = models.CharField(verbose_name='标签', max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
