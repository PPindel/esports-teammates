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


# class AddTeamAd(generic.CreateView):
#     model = TeamAd
#     template_name = 'add_team.html'
#     fields = ('title', 'author', 'game', 'role', 'skill_level', 'description', 'status')  # noqa E501


def add_new_ad(request):
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


# @method_decorator(login_required, name='dispatch')
# class EditTeamAd(generic.UpdateView):
#     model = TeamAd
#     template_name = 'edit_team.html'
#     fields = ('title', 'game', 'role', 'skill_level', 'description')

    # def get(self, request, slug, *args, **kwargs):
    #     queryset = TeamAd.objects.filter(status=1)
    #     team = get_object_or_404(queryset, slug=slug)

    #     return render(
    #         request,
    #         'edit_team.html',
    #         {
    #             'team': team
    #         },
    #     )

    # def get_success_url(self, request, *args, **kwargs):
    #     return reverse('team_detail', kwargs={'slug': self.object.slug})


# class EditComment(generic.UpdateView):
#     model = Comment
#     template_name = 'edit_comment.html'
#     fields = ('body',)


@method_decorator(login_required, name='dispatch')
class EditTeamAd(generic.UpdateView):
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

    # def edit_ad(request):
    #     if request.method == 'GET':
    #         context = {'form': TeamAdEdit(instance=post), }
    #         return render(request, 'edit_team.html', context)

    #     elif request.method == 'POST':
    #         team = get_object_or_404(queryset, slug=slug)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'The ad has been updated successfully.')  # noqa E501
    #             return redirect('team_detail', obj.slug)
    #         else:
    #             messages.error(request, 'Please correct the following errors:')  # noqa E501
    #             return render(request, 'edit_team.html', {'form': form, })

    # def get_success_url(self, request, *args, **kwargs):
    #     return reverse('team_detail', kwargs={'slug': self.object.slug})


@method_decorator(login_required, name='dispatch')
class EditComment(generic.UpdateView):
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
    model = Comment
    template_name = 'delete_comment.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your comment has been deleted.')
        return super(DeleteComment, self).delete(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        TeamDetail.comment_deleted = True
        return reverse('team_detail', kwargs={'slug': self.object.post.slug})

# class DeleteComment(generic.DeleteView):
#     model = Comment
#     template_name = 'delete_comment.html'
#     success_url = reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class DeleteTeamAd(generic.DeleteView):
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
    return render(request, 'profile.html')


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
