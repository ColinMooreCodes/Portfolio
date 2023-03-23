from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.


class User(AbstractUser):
    pass


class Post(models.Model):
    title = models.CharField(max_length=255)
    hasTags = models.BooleanField(blank=True)
    postBody = models.TextField()
    datePosted = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=[("public", "public"), ("draft", "draft"),
                 ("private", "private")],
        max_length=15)

    class Meta:
        abstract = True


class BlogPost(Post):
    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    class Meta:
        abstract = True


class BlogTag(Tag):
    onPost = models.ForeignKey(BlogPost, on_delete=models.PROTECT)


class GalleryPost(Post):
    primaryImage = models.ImageField(upload_to='gallery/images/')
    thumbnail = models.ImageField(upload_to='gallery/thumbs/')


class GalleryTag(Tag):
    onPost = models.ForeignKey(GalleryPost, on_delete=models.PROTECT)


class HeroSection(Post):
    startDate = models.DateField()
    endDate = models.DateField()


class Link(models.Model):
    platform = models.CharField(max_length=100)
    isActive = models.BooleanField()
    profileLink = models.CharField(max_length=255)
    thumbImg = models.CharField(max_length=300)

    class Meta:
        abstract = True


class ShopLink(Link):
    launch = models.DateField()


class SocialMedia(Link):
    username = models.CharField(max_length=100)
