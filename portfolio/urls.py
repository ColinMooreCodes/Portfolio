from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.panelLogin, name="login"),
    path("logout", views.panelLogout, name="logout"),
    path("panel", views.controlPanel, name="panel"),
    path("panel/new/<str:postType>", views.makeNewPost, name="new"),
    path("panel/manage/<str:postType>", views.managePosts, name="manage"),
    path("blog/", views.blogs, name="blog"),
    path("blog/<int:postid>", views.blogpost, name="blogpost"),
    path("gallery/<int:postid>", views.gallpost, name="gallerypost"),
    path("article/<int:postid>", views.article, name="article"),
    path("edit/<str:postType>/<int:postid>", views.edit, name="edit")
]
