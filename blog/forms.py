#!/usr/bin/env python
""" Script for writing the forms for the blog application """
from ckeditor.widgets import CKEditorWidget
from blog import models as md
from django import forms



class TagBlogForm(forms.ModelForm):

    class Meta:
        model = md.TagBlog
        fields = ['name', 'description']

class BlogForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = md.Blog
        fields = ['title', 'main_image', 'content', 'published', 'tags']

class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = md.BlogComment
        fields = ['name', 'email', 'comment']
