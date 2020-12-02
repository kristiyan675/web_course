from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=20)
    title_tag = models.CharField(max_length=20, default='Crypto Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by author: {self.author} with pk: {self.pk}"

    def get_absolute_url(self):
        return reverse('article_detail', args=str(self.id))
