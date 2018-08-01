from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('indexpolls', views.indexpolls, name='indexpolls'),
    path('<int:question_id>/detail/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/results/', views.vote, name='vote'),


    ]
