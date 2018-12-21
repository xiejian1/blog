from django.conf.urls import url
from django.conf.urls.static import static

from blog.views import index,detail,archives,category
from blogproject import settings
app_name = 'blog'
urlpatterns = [
    url(r'index/$',index,name='list'),
    url(r'post/(?P<pk>\d+)/$',detail,name='detail'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',archives,name='archives'),
    url(r'category/(?P<pk>\d+)/$',category,name='category'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)