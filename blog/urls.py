from . import views
from django.urls import path


urlpatterns = [
    path('', views.TeamList.as_view(), name='home')
]
