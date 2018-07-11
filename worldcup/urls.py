from django.urls import path
from . import views

app_name = 'worldcup'

urlpatterns = [
    path('', views.index, name='index'),
    path('scores/', views.scores, name='scores'),
    path('twitter/', views.twitterfeed, name='twitter'),
    path('teams/', views.search_team, name="teams")
]