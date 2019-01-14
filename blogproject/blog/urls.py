from django.conf.urls import url
from django.conf.urls.static import static

from blog.views import archives,IndexView,CategoryView,DetailPostView,TagView,search
from blogproject import settings
app_name = 'blog'
urlpatterns = [
    # url(r'index/$',index,name='list'),
    url(r'index/$',IndexView.as_view(),name='list'),
    # url(r'post/(?P<pk>\d+)/$',detail,name='detail'),
    url(r'post/(?P<pk>\d+)/$',DetailPostView.as_view(),name='detail'),
    url(r'archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',archives,name='archives'),
    # url(r'category/(?P<pk>\d+)/$',category,name='category'),
    url(r'category/(?P<pk>\d+)/$',CategoryView.as_view(),name='category'),
    url(r'^tag/(?P<pk>\d+)/$', TagView.as_view(), name='tag'),
    # url(r'^blogsearch/$',search,name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)