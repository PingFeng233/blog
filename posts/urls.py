from django.conf.urls import url
from .views import index, detail, categories, search, about

urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index, name='index'),
    url(r'^detail/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^cate/(?P<pk>\d+)/$', categories, name='categories'),
    url(r'^search/$', search, name='search'),
    url(r'^about/$', about, name='about')
]
