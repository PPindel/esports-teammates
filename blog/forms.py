from .models import Comment, TeamAd
from django import forms
from django.views.generic import CreateView


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class TeamAdForm(forms.ModelForm):
    class Meta:
        model = TeamAd
        fields = ['title', 'author', 'game', 'role', 'skill_level', 'description', 'status']  # noqa E501
