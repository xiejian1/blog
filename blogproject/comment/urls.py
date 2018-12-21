from django.conf.urls import url

from comment import views

app_name = 'comment'
urlpatterns = [
    url(r'post/(?P<post_pk>\d+)/$', views.post_comment, name='post_comment'),
]