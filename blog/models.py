from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from uuid import uuid4


class TagBlog(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)
    background_color = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class Blog(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    main_image = models.ImageField(upload_to='images/blogs', null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(TagBlog)
    views = models.IntegerField(default=0)

    class Meta:
        ordering = ['title']


class BlogComment(models.Model):
    id = models.UUIDField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created"]

