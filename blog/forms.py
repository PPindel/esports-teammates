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
        fields = ['title', 'game', 'role', 'skill_level', 'description', 'status']  # noqa E501


class TeamAdEdit(forms.ModelForm):
    class Meta:
        model = TeamAd
        fields = ('title', 'game', 'role', 'skill_level', 'description')


class CommentEdit(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
