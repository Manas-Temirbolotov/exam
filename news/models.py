from django.db import models
from django.db.models import Count

from account.models import Author


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def get_status(self, NewsStatus=None):
        statuses = NewsStatus.objects.filter(news=self) \
            .values('status__name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']
        return result


class Comment(models.Model):
    text = models.TextField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def get_status(self):
        statuses = CommentStatus.objects.filter(comment=self) \
            .values('status__name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']

        return result


class Status(models.Model):
    slug = models.SlugField(max_length=50, unique=True)
    name = models.CharField(max_length=50)


class NewStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, unique=True, on_delete=models.CASCADE)
    news = models.ForeignKey(News,unique=True, on_delete=models.CASCADE)


class CommentStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, unique=True, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, unique=True, on_delete=models.CASCADE)



