from django.urls import path

from . import views


urlpatterns = [
    path('', views.get_active_polls, name='active_polls'),
]
