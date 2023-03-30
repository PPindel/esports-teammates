from . import views
from django.urls import path


urlpatterns = [
    path('', views.TeamList.as_view(), name='home'),
    path('add_team/', views.add_new_ad, name='add_team'),
    path('<slug:slug>/', views.TeamDetail.as_view(), name='team_detail'),
    path('edit_team/<slug:slug>/', views.EditTeamAd.as_view(), name='edit_team'),  # noqa E501
    path('edit_comment/<int:pk>', views.EditComment.as_view(), name='edit_comment'),  # noqa E501
]
