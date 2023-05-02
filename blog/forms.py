from .models import Comment, TeamAd
from django import forms
from django.views.generic import CreateView
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.db import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class TeamAdForm(forms.ModelForm):
    class Meta:
        model = TeamAd
        fields = ['title', 'game', 'role', 'skill_level', 'description', 'featured_image']  # noqa E501


class TeamAdEdit(forms.ModelForm):
    class Meta:
        model = TeamAd
        fields = ('title', 'game', 'role', 'skill_level', 'description')


class CommentEdit(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
