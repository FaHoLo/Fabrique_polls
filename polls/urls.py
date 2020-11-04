from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


urlpatterns = [
    path('polls/active/', views.get_active_polls, name='active_polls'),
    path('polls/user/<int:user_id>', views.get_user_voted_polls, name='user_polls'),
    path('vote/', views.get_user_vote, name='user_vote')
]

router = DefaultRouter()
router.register('polls', views.PollsViewSet)
router.register('questions', views.QuestionsViewSet)

urlpatterns.extend([
    path('', include(router.urls)),
])
