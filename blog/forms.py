from .models import Comment, TeamAd
from django import forms
from django.views.generic import CreateView
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.db import models


class CommentForm(forms.ModelForm):
    """
    Comment form class
    Allows to write a comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class TeamAdForm(forms.ModelForm):
    """
    Team Ad form template
    Displays required fields to create a new Team Ad
    """
    class Meta:
        model = TeamAd
        fields = ['title', 'game', 'role', 'skill_level', 'description', 'featured_image']  # noqa E501


class TeamAdEdit(forms.ModelForm):
    """
    Team Ad edit class
    Allows to edit a Team Ad
    """
    class Meta:
        model = TeamAd
        fields = ('title', 'game', 'role', 'skill_level', 'description')


class CommentEdit(forms.ModelForm):
    """
    Comment edit class
    Allows to edit a Comment
    """
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    """
    Extends default django singup form
    """
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
