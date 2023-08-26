from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db import models
from uuid import uuid4


class TagTutorial(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField(null=True)

    def save(self, *args, **kwargs):
        self.id = uuid4()
        return super().save(*args, **kwargs)

class Tutorial(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.id = uuid4()
        return super().save(*args, **kwargs)



class TutorialContent(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='images/blogs', null=True)
    content = RichTextField()
    published = models.BooleanField(default=False)
    publish_date = models.DateField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(TagTutorial)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, null=True)

    def save(self, *args, **kwargs):
        self.id = uuid4()
        return super().save(*args, **kwargs)


    class Meta:
        ordering = ['title']


class TutorialComment(models.Model):
    id = models.UUIDField(primary_key=True)
    tutorial = models.ForeignKey(TutorialContent, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, null=False)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        self.id = uuid4()
        return super().save(*args, **kwargs)

