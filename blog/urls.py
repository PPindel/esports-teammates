from . import views
from django.urls import path


urlpatterns = [
    path('', views.TeamList.as_view(), name='home'),
    path('add_team/', views.AddTeamAd.as_view(), name='add_team'),
    path('<slug:slug>/', views.TeamDetail.as_view(), name='team_detail'),
]
