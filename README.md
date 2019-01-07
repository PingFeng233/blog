# blog

之前买了个云服务器，一直放在那里没怎么用，最近想着还是写个简单的博客放上去，不然太浪费了。

博客已经用openresty+gunicorn部署上去了。源码就是github上的这个项目了，这个数据库是我测试的数据库，跟我博客上的不太一样。

如果要用这个博客的源码，记得要先python manage.py makemigrations 和 python manage.py migrate 进行数据迁移。

部署到服务器上的方法，我在博客上写了一个教程：http:www.pfblog.top/detail/6/

博客地址：http:www.pfblog.top
