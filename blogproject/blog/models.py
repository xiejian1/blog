import markdown
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.html import strip_tags


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=77)
    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,null=True,blank=True)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #统计文章的阅读量
    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def increase_view(self):
        self.views = self.views+1
        self.save(update_fields=['views'])

    class Meta:
        ordering = ['-created_time']

    def save(self,*args,**kwargs):
        if not self.excerpt:
            mk = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = strip_tags(mk.convert(self.body))[:200]
        super(Post,self).save(*args,**kwargs)



