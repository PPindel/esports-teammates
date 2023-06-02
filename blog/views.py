from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import TeamAd, Comment
from .forms import CommentForm, TeamAdForm, CommentEdit, TeamAdEdit
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy


class TeamList(generic.ListView):
    """
    List view of Team Ads
    Has pagination
    No authentication required
    """
    model = TeamAd
    queryset = TeamAd.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class TeamDetail(View):
    """
    Allows to display TeamAd page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = TeamAd.objects.filter(status=1)
        team = get_object_or_404(queryset, slug=slug)
        comments = team.comments.filter(approved=True).order_by('created_on')

        return render(
            request,
            'team_detail.html',
            {
                'team': team,
                'comments': comments,
                'commented': False,
                'comment_form': CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = TeamAd.objects.filter(status=1)
        team = get_object_or_404(queryset, slug=slug)
        comments = team.comments.filter(approved=True).order_by('created_on')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = team
            comment.save()
            messages.add_message(request, messages.INFO, 'SUCCESS!')
        else:
            comment_from = CommentForm()

        return render(
            request,
            'team_detail.html',
            {
                'team': team,
                'comments': comments,
                'commented': True,
                'comment_form': CommentForm()
            },
        )


def add_new_ad(request):
    """
    Allows to create a new ad
    """
    form = TeamAdForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':

        if form.is_valid():

            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            form = TeamAdForm()
            messages.success(request, 'Successfully created')
            return redirect('team_detail', obj.slug)

    return render(request, 'add_team.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class EditTeamAd(generic.UpdateView):
    """
    Allows to edit an ad
    Authentication required
    """
    model = TeamAd
    form_class = TeamAdEdit
    template_name = 'edit_team.html'

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, 'Successfully edited!')
        return HttpResponseRedirect(self.get_success_url())

    def get(self, request, slug, *args, **kwargs):
        queryset = TeamAd.objects.filter(status=1)
        team = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'edit_team.html',
            {
                'team': team,
                'form': TeamAdEdit(instance=team)
            },
        )


@method_decorator(login_required, name='dispatch')
class EditComment(generic.UpdateView):
    """
    Allows to edit a comment
    Authentication required
    """
    model = Comment
    form_class = CommentEdit
    template_name = 'edit_comment.html'

    def form_valid(self, form):
        super().form_valid(form)
        messages.success(self.request, 'Successfully edited!')
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self, *args, **kwargs):
        TeamDetail.comment_edited = True
        return reverse('team_detail', kwargs={'slug': self.object.post.slug})


@method_decorator(login_required, name='dispatch')
class DeleteComment(generic.DeleteView):
    """
    Allows to delete a comment
    Authentication required
    """
    model = Comment
    template_name = 'delete_comment.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your comment has been deleted.')
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        TeamDetail.comment_deleted = True
        return reverse('team_detail', kwargs={'slug': self.object.post.slug})


@method_decorator(login_required, name='dispatch')
class DeleteTeamAd(generic.DeleteView):
    """
    Allows to delete an ad
    Authentication required
    """
    model = TeamAd
    template_name = 'delete_team.html'

    def get(self, request, slug, *args, **kwargs):
        queryset = TeamAd.objects.filter(status=1)
        team = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            'delete_team.html',
            {
                'team': team,
            },
        )

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your ad has been deleted.')
        return super(DeleteTeamAd, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        TeamDetail.team_deleted = True
        return reverse('home')


def profile(request):
    """
    Displays profile page
    """
    return render(request, 'profile.html')


def error_403_view(request, exception):
    """
    Displays 403.html path
    """

    return render(request, '403.html')


def error_404_view(request, exception):
    """
    Displays 404.html path
    """

    return render(request, '404.html')


def handler500(request, *args, **argv):
    """
    Displays 500.html path
    """
    return render(request, '500.html')
