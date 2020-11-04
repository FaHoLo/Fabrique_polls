from django.urls import path

from . import views


urlpatterns = [
    path('polls/active/', views.get_active_polls, name='active_polls'),
    path('polls/user/<int:user_id>', views.get_user_voted_polls, name='user_polls'),
    path('vote/', views.get_user_vote, name='user_vote')
]
