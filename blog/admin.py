from django.contrib import admin
from .models import TeamAd
from django_summernote.admin import SummernoteModelAdmin


@admin.register(TeamAd)
class TeamAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')
