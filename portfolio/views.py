from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.paginator import Paginator
import os

from .models import BlogPost, GalleryPost, HeroSection, GalleryTag, BlogTag
import re

# Create your views here.


class newPost(forms.Form):
    title = forms.CharField(label="Title", label_suffix="")
    tags = forms.CharField(label="Tags", label_suffix="", required=False)
    body = forms.CharField(widget=forms.Textarea,
                           label="Post", label_suffix="")
    status = forms.ChoiceField(
        choices=(("draft", "draft"), ("public", "public"),
                 ("private", "private")), label_suffix=""
    )


class newGallPost(newPost):
    image = forms.FileField(label="Image", label_suffix="")
    thumbnail = forms.FileField(label="Thumbnail", label_suffix="")


class newHero(newPost):
    startDate = forms.DateTimeField(label="Start Date", label_suffix="")
    endDate = forms.DateTimeField(label="End Date", label_suffix="")


def index(request):
    blogs = getPosts("blog", 2, "public")
    arts = getPosts("gallery", 6, "public")
    return render(request, "portfolio/index.html", {
        "blogPosts": blogs,
        "artPosts": arts
    })


def blogs(request):
    blogs = getPosts("blog", 0, "public")
    paginator = Paginator(blogs, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "portfolio/viewposts.html", {
        "type": "blogs",
        "page_obj": page_obj
        # "blogPosts": blogs
    })


def panelLogin(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('panel')
        else:
            return render(request, "portfolio/panelLogin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "portfolio/panelLogin.html")


def panelLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


@login_required
def controlPanel(request):

    return render(request, "portfolio/panel.html")


@login_required
def makeNewPost(request, postType):
    if request.method == 'POST':
        formData = request.POST
        title = formData['title']
        tags = formData['tags']
        body = formData['body']
        status = formData['status']
        postTable = None
        tagTable = None
        hasTags = False
        if tags != '':
            hasTags = True
        post = None
        if postType == 'blog':
            post = BlogPost(title=title, postBody=body,
                            status=status, hasTags=hasTags)
            postTable = BlogPost
            tagTable = BlogTag
        elif postType == 'gallery':
            image = request.FILES['image']
            thumb = request.FILES['thumbnail']
            post = GalleryPost(title=title, postBody=body,
                               status=status, hasTags=hasTags, primaryImage=image, thumbnail=thumb)
            postTable = GalleryPost
            tagTable = GalleryTag
        try:
            post.save()
            posted = postTable.objects.latest('id')
            messages.success(request, 'Blog post posted successfully')
            if tags != '':
                print("Processing tags")
                splitTags = tags.split(',')
                processTags(request, tagTable, postTable, splitTags, posted.id)
            return HttpResponseRedirect(reverse(postType, args=[posted.id]))
        except:
            messages.error(request, 'Could not save post')
    if postType == 'gallery':
        form = newGallPost()
    elif postType == 'hero':
        form = newHero()
    else:
        form = newPost()
    return render(request, "portfolio/panelMakePost.html", {
        "type": postType,
        "form": form
    })


@login_required
def managePosts(request, postType):
    posts = getPosts(postType, 0, "all")
    return render(request, "portfolio/panelManage.html", {
        "type": postType,
        "posts": posts
    })


@login_required
def blogpost(request, postid):
    blogPost = getSinglePost("blog", postid)
    return render(request, "portfolio/post.html", {
        "post": blogPost
    })


@login_required
def gallpost(request, postid):
    gallPost = getSinglePost("gallery", postid)
    return render(request, "portfolio/post.html", {
        "post": gallPost,
        "postType": 'gallery'
    })


@login_required
def article(request, id):
    pass


@login_required
def edit(request, postType, id):
    pass


def getPosts(postType, limit, status):
    postsTable = None
    tagsTable = None
    posts = []
    if postType == "gallery":
        postsTable = GalleryPost
        tagsTable = GalleryTag
    else:
        postsTable = BlogPost
        tagsTable = BlogTag
    if limit > 0:
        if status == "public":
            postsDB = postsTable.objects.filter(
                status="public").order_by("-datePosted")[:limit]
        else:
            postsDB = postsTable.objects.order_by("-datePosted")[:limit]
    else:
        if status == "public":
            postsDB = postsTable.objects.filter(
                status="public").order_by("-datePosted")
        else:
            postsDB = postsTable.objects.order_by("-datePosted")
    for item in postsDB:
        post = {
            "title": item.title,
            "body": item.postBody,
            "date": item.datePosted,
            "status": item.status,
            "id": item.id
        }
        if postType == "gallery":
            post["image"] = item.primaryImage.url
            post["thumb"] = item.thumbnail.url
        if item.hasTags:
            tags = []
            postTags = tagsTable.objects.filter(onPost=item.id)
            for tag in postTags:
                tag = {
                    "tag": tag.tag,
                    "slug": tag.slug
                }
                tags.append(tag)
            post["tags"] = tags
        else:
            post.tags = [
                {
                    "tag": "uncategorized",
                    "slug": "uncategorized"
                }
            ]
        posts.append(post)
    return posts


def getSinglePost(postType, postid):
    postsTable = None
    tagsTable = None
    if postType == "gallery":
        postsTable = GalleryPost
        tagsTable = GalleryTag
    else:
        postsTable = BlogPost
        tagsTable = BlogTag
    postDB = postsTable.objects.get(id=postid)
    post = {
        "title": postDB.title,
        "body": postDB.postBody,
        "date": postDB.datePosted,
        "status": postDB.status,
        "id": postDB.id
    }
    if postType == "gallery":
        post["image"] = postDB.primaryImage.url
        post["thumb"] = postDB.thumbnail.url
    if postDB.hasTags:
        tags = []
        postTags = tagsTable.objects.filter(onPost=postDB.id)
        for tag in postTags:
            tag = {
                "tag": tag.tag,
                "slug": tag.slug
            }
            tags.append(tag)
        post["tags"] = tags
    else:
        post.tags = [
            {
                "tag": "uncategorized",
                "slug": "uncategorized"
            }
        ]
    return post


def processTags(request, tagTable, postTable, tags, postid):
    for tag in tags:
        print(tag)
        slug = re.sub(r'[^\w\s]', '', tag).strip().replace(' ', '-')
        addTag = tagTable(tag=tag, slug=slug, onPost=postTable(id=postid))
        try:
            addTag.save()
        except:
            messages.error(request, f"Cound not save the tag: {tag}")
