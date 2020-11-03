from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_active_polls, name='active_polls'),
    path('user/<int:user_id>', views.get_user_voted_polls, name='user_polls')

]
