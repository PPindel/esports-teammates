from . import views
from django.urls import path


urlpatterns = [
    path('', views.TeamList.as_view(), name='home'),
    path('add_team/', views.add_new_ad, name='add_team'),
    path('profile/', views.profile, name='profile'),
    path('edit_team/<slug:slug>/', views.EditTeamAd.as_view(), name='edit_team'),  # noqa E501
    path('delete_team/<slug:slug>/', views.DeleteTeamAd.as_view(), name='delete_team'),  # noqa E501
    path('edit_comment/<int:pk>/', views.EditComment.as_view(), name='edit_comment'),  # noqa E501
    path('delete_comment/<int:pk>/', views.DeleteComment.as_view(), name='delete_comment'),  # noqa E501
    path('team_detail/<slug:slug>/', views.TeamDetail.as_view(), name='team_detail'),  # noqa E501
    path('404', views.error_404_view, name='404'),
    path('500', views.handler500, name='500'),
]
