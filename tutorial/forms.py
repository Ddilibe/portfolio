#!/usr/bin/env python
""" Script for describing the forms for the models """

from tutorial import models as md
from django import forms


class TagTutorialForm(forms.ModelForm):

    class Meta:
        model = md.TagTutorial
        fields = ['name']

class TutorialForm(forms.ModelForm):

    class Meta:
        model = md.Tutorial
        fields = ['title', 'description']

class TutorialContentForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = md.TutorialContent
        fields = ['title', 'content', 'published', 'tags']

class TutorialCommentForm(forms.ModelForm):

    class Meta:
        model = md.TutorialComment
        fields = ['name', 'email', 'comment']
