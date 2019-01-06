from django.contrib.syndication.views import Feed

from blog.models import Post


class AllPostRssFeed(Feed):
    #显示在聚合阅读器上的标题
    title = "Django 博客"
    #通过聚合阅读器跳到网站的地址
    link = '/'
    #显示在聚合阅读器上的描述信息
    description = "Django 博客项目"
    #需要显示的内容条目
    def items(self):
        return Post.objects.all()
    #聚合阅读器器中显示的内容条目的标题
    def item_title(self,item):
        return "[%s] %s"%(item.category,item.title)
    #聚合阅读器中显示的内容条目的描述
    def item_description(self,item):
        return item.body