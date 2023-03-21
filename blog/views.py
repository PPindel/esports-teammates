from django.shortcuts import render
from django.views import generic
from .models import TeamAd


class TeamList(generic.ListView):
    model = TeamAd
    queryset = TeamAd.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
