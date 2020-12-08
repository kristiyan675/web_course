from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('home')


class Post(models.Model):
    title = models.CharField(max_length=20)
    title_tag = models.CharField(max_length=20, default='Crypto Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, default='coding')
    likes = models.ManyToManyField(User, related_name='block_post')


    def __str__(self):
        return f"{self.title} by author: {self.author} with pk: {self.pk}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])
