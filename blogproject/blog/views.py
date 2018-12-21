import markdown as markdown
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Post, Category


# Create your views here.
from comment.forms import CommentForm


def index(request):
    # post_list = Post.objects.all().order_by('-created_time')
    post_list = Post.objects.all()
    return render(request,'blog/index.html',{'post_list':post_list})

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #阅读量增加1
    post.increase_view()
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                                         'markdown.extensions.toc', ])
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,created_time__month=month).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
