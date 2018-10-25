from django.conf.urls import url
from .views import search

urlpatterns = [
    url('^videoplayer/search/$', search, name='search')
]
