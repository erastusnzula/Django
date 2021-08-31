from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Category'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField('Date Published')
    last_modified = models.DateTimeField('Date Modified')
    categories = models.ManyToManyField(Category, related_name='posts')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    edited = models.CharField(max_length=255, default='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.body[:100]}'
