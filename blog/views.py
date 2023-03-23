from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import TeamAd


class TeamList(generic.ListView):
    model = TeamAd
    queryset = TeamAd.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TeamDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = TeamAd.objects.filter(status=1)
        team = get_object_or_404(queryset, slug=slug)
        comments = team.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            "team_detail.html",
            {
                "team": team,
                "comments": comments,
            },
        )
