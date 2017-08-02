from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about',views.about, name='about'),
    url(r'^what_we_do',views.what_we_do, name='what_we_do'),
    url(r'^news',views.news, name='news'),
    url(r'^we_cares',views.we_cares, name='we_cares'),
    url(r'^help',views.help, name='help'),
    url(r'^contacts',views.contacts, name='contacts'),
    url(r'^article/(?P<article_id>\d+)/$', views.article, name='article'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)