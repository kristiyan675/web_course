from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('home')


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    website_url = models.CharField(max_length=200, null=True, blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    instagram_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class Post(models.Model):
    title = models.CharField(max_length=20)
    title_tag = models.CharField(max_length=20, default='Crypto Blog')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, default='coding')
    snippet = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='block_post')
    header_image = models.ImageField(null=True, blank=True, upload_to='images/')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.title} by author: {self.author} with pk: {self.pk}"

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.pk)])
