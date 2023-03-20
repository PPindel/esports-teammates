from django.contrib import admin
from .models import TeamAd, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(TeamAd)
class TeamAdmin(SummernoteModelAdmin):

    list_display = ('game', 'title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'description', 'game']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'game')
    summernote_fields = ('description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
